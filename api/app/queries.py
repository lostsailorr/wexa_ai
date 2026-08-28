"""
Comprehensive Cypher Queries for SentinelGraph.
All queries are parameterized to prevent injection and maximize engine plan caching.
"""

# 1. Circular Transaction Ring (Smurfing / Layering) Detection
# Traverses 3 to 6 hops of directed money transfers that cycle back to the starting account
CYPHER_CIRCULAR_RINGS = """
MATCH path = (origin:BankAccount)-[txs:TRANSFERRED_TO*3..6]->(origin)
WITH path, origin, txs,
     reduce(total = 0.0, t IN txs | total + t.amount) AS total_volume,
     [n IN nodes(path) | n.account_number] AS account_chain,
     [t IN txs | t.tx_id] AS transaction_chain
RETURN DISTINCT
    origin.account_number AS origin_account,
    origin.bank_name AS origin_bank,
    length(path) AS loop_length,
    total_volume,
    account_chain,
    transaction_chain,
    [n IN nodes(path) | {
        id: n.id,
        label: labels(n)[0],
        account_number: n.account_number,
        bank_name: n.bank_name,
        country: n.country,
        risk_level: n.risk_level
    }] AS ring_nodes,
    [r IN relationships(path) | {
        tx_id: r.tx_id,
        amount: r.amount,
        currency: r.currency,
        timestamp: r.timestamp,
        from_acc: startNode(r).account_number,
        to_acc: endNode(r).account_number
    }] AS ring_edges
ORDER BY loop_length ASC, total_volume DESC
LIMIT $limit
"""

# 2. Ultimate Beneficial Ownership (UBO) Recursive Resolution
# Unravels multi-tier ownership chains (Person -> Company -> Company -> Company)
# and calculates cumulative effective ownership percentage
CYPHER_UBO_RESOLVE = """
MATCH path = (root:Person)-[owns:OWNS*1..8]->(target:Company {id: $company_id})
WHERE NONE(n IN nodes(path)[1..-1] WHERE n:Person)
WITH root, target, path, owns,
     reduce(effective_pct = 1.0, r IN owns | effective_pct * (r.share_pct / 100.0)) * 100.0 AS effective_share_pct
WHERE effective_share_pct >= $min_share_pct
RETURN
    root.id AS ubo_id,
    root.name AS ubo_name,
    root.nationality AS nationality,
    root.is_pep AS is_pep,
    root.base_risk AS person_risk,
    target.id AS company_id,
    target.name AS company_name,
    round(effective_share_pct * 100.0) / 100.0 AS effective_ownership_pct,
    length(path) AS ownership_depth,
    [n IN nodes(path) | {
        id: n.id,
        name: n.name,
        type: labels(n)[0],
        risk_score: coalesce(n.risk_score, n.base_risk, 0.0),
        jurisdiction: coalesce(n.jurisdiction, n.nationality, 'Unknown')
    }] AS ownership_chain,
    [r IN relationships(path) | {
        share_pct: r.share_pct,
        since: r.since
    }] AS relationship_chain
ORDER BY effective_ownership_pct DESC
"""

# 3. Shortest Path to Sanctioned Entity or PEP
# Identifies the shortest connection through corporate ownership, accounts, or transfers to a blacklisted entity
CYPHER_SHORTEST_SANCTION_PATH = """
MATCH (start)
WHERE start.id = $entity_id OR start.account_number = $entity_id
MATCH (sanctioned:SanctionList)
MATCH path = shortestPath((start)-[*1..6]-(sanctioned))
WHERE length(path) > 0
RETURN
    length(path) AS distance,
    sanctioned.id AS sanction_id,
    sanctioned.authority AS sanctioning_body,
    sanctioned.program AS sanction_program,
    sanctioned.reason AS sanction_reason,
    [n IN nodes(path) | {
        id: coalesce(n.id, n.account_number),
        name: coalesce(n.name, n.account_number),
        label: labels(n)[0],
        risk_score: coalesce(n.risk_score, n.base_risk, 0.0),
        country: coalesce(n.jurisdiction, n.nationality, n.country, 'N/A')
    }] AS path_nodes,
    [r IN relationships(path) | {
        type: type(r),
        from_id: coalesce(startNode(r).id, startNode(r).account_number),
        to_id: coalesce(endNode(r).id, endNode(r).account_number),
        properties: properties(r)
    }] AS path_relationships
ORDER BY distance ASC
LIMIT 1
"""

# 4. Global Subgraph Retrieval (Filtered by risk and type for interactive canvas)
CYPHER_SUBGRAPH = """
MATCH (n)
WHERE ($type IS NULL OR labels(n)[0] = $type)
  AND ($min_risk IS NULL OR coalesce(n.risk_score, n.base_risk, 0.0) >= $min_risk)
OPTIONAL MATCH (n)-[r]->(m)
WHERE ($type IS NULL OR labels(m)[0] = $type OR m IS NOT NULL)
RETURN
    collect(DISTINCT {
        id: coalesce(n.id, n.account_number),
        label: labels(n)[0],
        name: coalesce(n.name, n.account_number),
        risk_score: coalesce(n.risk_score, n.base_risk, 0.0),
        properties: properties(n)
    }) AS nodes,
    collect(DISTINCT {
        id: id(r),
        type: type(r),
        source: coalesce(startNode(r).id, startNode(r).account_number),
        target: coalesce(endNode(r).id, endNode(r).account_number),
        properties: properties(r)
    }) AS edges
"""

# 5. Entity 360 Neighborhood Expansion (Depth 1 to 2)
CYPHER_ENTITY_NEIGHBORHOOD = """
MATCH (center)
WHERE center.id = $entity_id OR center.account_number = $entity_id
OPTIONAL MATCH path = (center)-[r*1..2]-(neighbor)
WITH center, collect(DISTINCT path) AS paths
UNWIND (CASE WHEN size(paths) > 0 THEN paths ELSE [null] END) AS p
WITH center,
     collect(DISTINCT CASE WHEN p IS NOT NULL THEN startNode(last(relationships(p))) ELSE center END) +
     collect(DISTINCT CASE WHEN p IS NOT NULL THEN endNode(last(relationships(p))) ELSE center END) AS all_nodes,
     collect(DISTINCT CASE WHEN p IS NOT NULL THEN last(relationships(p)) ELSE null END) AS all_rels
UNWIND all_nodes AS n
WITH DISTINCT n, all_rels
RETURN
    collect(DISTINCT {
        id: coalesce(n.id, n.account_number),
        label: labels(n)[0],
        name: coalesce(n.name, n.account_number),
        risk_score: coalesce(n.risk_score, n.base_risk, 0.0),
        properties: properties(n)
    }) AS nodes,
    [r IN all_rels WHERE r IS NOT NULL | {
        id: id(r),
        type: type(r),
        source: coalesce(startNode(r).id, startNode(r).account_number),
        target: coalesce(endNode(r).id, endNode(r).account_number),
        properties: properties(r)
    }] AS edges
"""

# 6. High-Betweenness Mule & Nexus Account Detection
# Finds accounts with high in-degree and out-degree acting as transit hubs
CYPHER_MULE_HUBS = """
MATCH (acc:BankAccount)
MATCH (in_acc:BankAccount)-[in_tx:TRANSFERRED_TO]->(acc)
MATCH (acc)-[out_tx:TRANSFERRED_TO]->(out_acc:BankAccount)
WITH acc,
     count(DISTINCT in_acc) AS unique_senders,
     count(DISTINCT out_acc) AS unique_recipients,
     sum(in_tx.amount) AS total_inflow,
     sum(out_tx.amount) AS total_outflow
WHERE unique_senders >= 2 AND unique_recipients >= 2
RETURN
    acc.account_number AS account_number,
    acc.bank_name AS bank_name,
    acc.country AS country,
    acc.risk_level AS risk_level,
    unique_senders,
    unique_recipients,
    total_inflow,
    total_outflow,
    abs(total_inflow - total_outflow) AS net_retention,
    (unique_senders * unique_recipients * 1.5) AS centrality_index
ORDER BY centrality_index DESC
LIMIT $limit
"""

# 7. Database Summary Metrics
CYPHER_SUMMARY_METRICS = """
MATCH (n)
WITH count(n) AS total_nodes,
     count(DISTINCT CASE WHEN n:Person THEN n END) AS person_count,
     count(DISTINCT CASE WHEN n:Company THEN n END) AS company_count,
     count(DISTINCT CASE WHEN n:BankAccount THEN n END) AS account_count,
     count(DISTINCT CASE WHEN n:SanctionList THEN n END) AS sanction_count,
     count(DISTINCT CASE WHEN n:Jurisdiction THEN n END) AS jurisdiction_count
OPTIONAL MATCH ()-[r]->()
WITH total_nodes, person_count, company_count, account_count, sanction_count, jurisdiction_count,
     count(r) AS total_relationships,
     count(DISTINCT CASE WHEN type(r) = 'TRANSFERRED_TO' THEN r END) AS transfer_count,
     count(DISTINCT CASE WHEN type(r) = 'OWNS' THEN r END) AS ownership_count
RETURN {
    total_nodes: total_nodes,
    person_count: person_count,
    company_count: company_count,
    account_count: account_count,
    sanction_count: sanction_count,
    jurisdiction_count: jurisdiction_count,
    total_relationships: total_relationships,
    transfer_count: transfer_count,
    ownership_count: ownership_count
} AS summary
"""
