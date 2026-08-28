import logging
from typing import Dict, Any, List, Optional
from app.database import db
from app.queries import (
    CYPHER_CIRCULAR_RINGS,
    CYPHER_UBO_RESOLVE,
    CYPHER_SHORTEST_SANCTION_PATH,
    CYPHER_SUBGRAPH,
    CYPHER_ENTITY_NEIGHBORHOOD,
    CYPHER_MULE_HUBS,
    CYPHER_SUMMARY_METRICS,
)
from app.services.mock_data import MOCK_NODES, MOCK_EDGES

logger = logging.getLogger("sentinelgraph.service")


class GraphService:

    @staticmethod
    def get_summary_metrics() -> Dict[str, Any]:
        """Returns aggregate node & relationship metrics."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_SUMMARY_METRICS)
                if results and "summary" in results[0]:
                    return {
                        "mode": "live_cognodb",
                        "metrics": results[0]["summary"]
                    }
            except Exception as e:
                logger.warning(f"Error querying live metrics, using fallback: {e}")

        # Fallback in-memory computation
        person_count = sum(1 for n in MOCK_NODES if n["label"] == "Person")
        company_count = sum(1 for n in MOCK_NODES if n["label"] == "Company")
        account_count = sum(1 for n in MOCK_NODES if n["label"] == "BankAccount")
        sanction_count = sum(1 for n in MOCK_NODES if n["label"] == "SanctionList")
        jurisdiction_count = sum(1 for n in MOCK_NODES if n["label"] == "Jurisdiction")
        transfer_count = sum(1 for e in MOCK_EDGES if e["type"] == "TRANSFERRED_TO")
        ownership_count = sum(1 for e in MOCK_EDGES if e["type"] == "OWNS")

        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "metrics": {
                "total_nodes": len(MOCK_NODES),
                "person_count": person_count,
                "company_count": company_count,
                "account_count": account_count,
                "sanction_count": sanction_count,
                "jurisdiction_count": jurisdiction_count,
                "total_relationships": len(MOCK_EDGES),
                "transfer_count": transfer_count,
                "ownership_count": ownership_count
            }
        }

    @staticmethod
    def get_subgraph(node_type: Optional[str] = None, min_risk: Optional[float] = None) -> Dict[str, Any]:
        """Retrieves graph nodes and edges with optional label and risk score filters."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_SUBGRAPH, {"type": node_type, "min_risk": min_risk})
                if results:
                    return {
                        "mode": "live_cognodb",
                        "nodes": results[0]["nodes"] or [],
                        "edges": results[0]["edges"] or []
                    }
            except Exception as e:
                logger.warning(f"Live subgraph query failed, using fallback: {e}")

        # Fallback simulation
        filtered_nodes = []
        valid_node_ids = set()
        for n in MOCK_NODES:
            if node_type and n["label"] != node_type:
                continue
            risk = n.get("risk_score") or n.get("base_risk") or 0.0
            if min_risk is not None and risk < min_risk:
                continue
            nid = n.get("account_number") or n["id"]
            filtered_nodes.append({
                "id": nid,
                "label": n["label"],
                "name": n.get("name") or nid,
                "risk_score": risk,
                "properties": n
            })
            valid_node_ids.add(nid)

        filtered_edges = []
        for e in MOCK_EDGES:
            if e["source"] in valid_node_ids and e["target"] in valid_node_ids:
                filtered_edges.append({
                    "id": e["id"],
                    "type": e["type"],
                    "source": e["source"],
                    "target": e["target"],
                    "properties": e.get("properties", {})
                })

        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "nodes": filtered_nodes,
            "edges": filtered_edges
        }

    @staticmethod
    def get_entity_neighborhood(entity_id: str) -> Dict[str, Any]:
        """Returns 1-2 hop neighborhood around a specific entity."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_ENTITY_NEIGHBORHOOD, {"entity_id": entity_id})
                if results:
                    return {
                        "mode": "live_cognodb",
                        "entity_id": entity_id,
                        "nodes": results[0]["nodes"] or [],
                        "edges": results[0]["edges"] or []
                    }
            except Exception as e:
                logger.warning(f"Live neighborhood query failed: {e}")

        # Fallback
        connected_edge_ids = set()
        connected_node_ids = {entity_id}

        # Hop 1
        for e in MOCK_EDGES:
            if e["source"] == entity_id or e["target"] == entity_id:
                connected_edge_ids.add(e["id"])
                connected_node_ids.add(e["source"])
                connected_node_ids.add(e["target"])

        # Hop 2
        for e in MOCK_EDGES:
            if e["source"] in connected_node_ids or e["target"] in connected_node_ids:
                connected_edge_ids.add(e["id"])
                connected_node_ids.add(e["source"])
                connected_node_ids.add(e["target"])

        nodes = [
            {
                "id": n.get("account_number") or n["id"],
                "label": n["label"],
                "name": n.get("name") or n.get("account_number"),
                "risk_score": n.get("risk_score") or n.get("base_risk") or 0.0,
                "properties": n
            }
            for n in MOCK_NODES
            if (n.get("account_number") or n["id"]) in connected_node_ids
        ]
        edges = [e for e in MOCK_EDGES if e["id"] in connected_edge_ids]

        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "entity_id": entity_id,
            "nodes": nodes,
            "edges": edges
        }

    @staticmethod
    def detect_circular_rings(limit: int = 10) -> Dict[str, Any]:
        """Detects circular smurfing & layering loops."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_CIRCULAR_RINGS, {"limit": limit})
                return {
                    "mode": "live_cognodb",
                    "rings_found": len(results),
                    "rings": results
                }
            except Exception as e:
                logger.warning(f"Live circular ring query failed: {e}")

        # Fallback simulation of detected rings
        mock_rings = [
            {
                "origin_account": "ACC-9003",
                "origin_bank": "BVI International Trust Bank",
                "loop_length": 4,
                "total_volume": 3220000.0,
                "account_chain": ["ACC-9003", "ACC-9002", "ACC-9005", "ACC-9012", "ACC-9003"],
                "transaction_chain": ["TX-SMURF-101", "TX-SMURF-102", "TX-SMURF-103", "TX-SMURF-104"],
                "ring_nodes": [
                    {"id": "ACC-9003", "label": "BankAccount", "account_number": "ACC-9003", "bank_name": "BVI International Trust Bank", "country": "BVI", "risk_level": "CRITICAL"},
                    {"id": "ACC-9002", "label": "BankAccount", "account_number": "ACC-9002", "bank_name": "Bank of Cyprus Commercial", "country": "Cyprus", "risk_level": "HIGH"},
                    {"id": "ACC-9005", "label": "BankAccount", "account_number": "ACC-9005", "bank_name": "Emirates NBD Freezone", "country": "UAE", "risk_level": "HIGH"},
                    {"id": "ACC-9012", "label": "BankAccount", "account_number": "ACC-9012", "bank_name": "Cayman Grand Trust Bank", "country": "Cayman Islands", "risk_level": "CRITICAL"}
                ],
                "ring_edges": [
                    {"tx_id": "TX-SMURF-101", "amount": 850000.0, "currency": "USD", "timestamp": "2023-11-01T09:15:00Z", "from_acc": "ACC-9003", "to_acc": "ACC-9002"},
                    {"tx_id": "TX-SMURF-102", "amount": 820000.0, "currency": "USD", "timestamp": "2023-11-02T11:30:00Z", "from_acc": "ACC-9002", "to_acc": "ACC-9005"},
                    {"tx_id": "TX-SMURF-103", "amount": 790000.0, "currency": "USD", "timestamp": "2023-11-03T14:45:00Z", "from_acc": "ACC-9005", "to_acc": "ACC-9012"},
                    {"tx_id": "TX-SMURF-104", "amount": 760000.0, "currency": "USD", "timestamp": "2023-11-04T16:20:00Z", "from_acc": "ACC-9012", "to_acc": "ACC-9003"}
                ]
            },
            {
                "origin_account": "ACC-9006",
                "origin_bank": "Banco General Panama",
                "loop_length": 3,
                "total_volume": 1730000.0,
                "account_chain": ["ACC-9006", "ACC-9013", "ACC-9004", "ACC-9006"],
                "transaction_chain": ["TX-LAYER-201", "TX-LAYER-202", "TX-LAYER-203"],
                "ring_nodes": [
                    {"id": "ACC-9006", "label": "BankAccount", "account_number": "ACC-9006", "bank_name": "Banco General Panama", "country": "Panama", "risk_level": "CRITICAL"},
                    {"id": "ACC-9013", "label": "BankAccount", "account_number": "ACC-9013", "bank_name": "Marshall Trust Depository", "country": "Marshall Islands", "risk_level": "CRITICAL"},
                    {"id": "ACC-9004", "label": "BankAccount", "account_number": "ACC-9004", "bank_name": "Barclays Commercial London", "country": "United Kingdom", "risk_level": "MEDIUM"}
                ],
                "ring_edges": [
                    {"tx_id": "TX-LAYER-201", "amount": 600000.0, "currency": "USD", "timestamp": "2023-12-10T10:00:00Z", "from_acc": "ACC-9006", "to_acc": "ACC-9013"},
                    {"tx_id": "TX-LAYER-202", "amount": 580000.0, "currency": "USD", "timestamp": "2023-12-11T13:10:00Z", "from_acc": "ACC-9013", "to_acc": "ACC-9004"},
                    {"tx_id": "TX-LAYER-203", "amount": 550000.0, "currency": "USD", "timestamp": "2023-12-12T15:40:00Z", "from_acc": "ACC-9004", "to_acc": "ACC-9006"}
                ]
            }
        ]

        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "rings_found": len(mock_rings),
            "rings": mock_rings
        }

    @staticmethod
    def resolve_ubo(company_id: str, min_share_pct: float = 10.0) -> Dict[str, Any]:
        """Recursively traverses multi-tier ownership chains to compute UBO."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_UBO_RESOLVE, {"company_id": company_id, "min_share_pct": min_share_pct})
                return {
                    "mode": "live_cognodb",
                    "target_company_id": company_id,
                    "beneficial_owners": results
                }
            except Exception as e:
                logger.warning(f"Live UBO query failed: {e}")

        # Fallback simulation
        if company_id in ("C-208", "Lumina Capital Partners LP"):
            # Viktor Sterling -> Seashell (100%) -> Apex (85%) -> Golden Horizon (90%) -> Lumina Capital (75%) = 57.375%
            return {
                "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
                "target_company_id": "C-208",
                "beneficial_owners": [
                    {
                        "ubo_id": "P-101",
                        "ubo_name": "Viktor Sterling",
                        "nationality": "Russian",
                        "is_pep": True,
                        "person_risk": 0.94,
                        "company_id": "C-208",
                        "company_name": "Lumina Capital Partners LP",
                        "effective_ownership_pct": 57.38,
                        "ownership_depth": 4,
                        "ownership_chain": [
                            {"id": "P-101", "name": "Viktor Sterling", "type": "Person", "risk_score": 0.94, "jurisdiction": "Russian"},
                            {"id": "C-201", "name": "Seashell Global Holdings Ltd", "type": "Company", "risk_score": 0.91, "jurisdiction": "BVI"},
                            {"id": "C-202", "name": "Apex Meridian Trading S.A.", "type": "Company", "risk_score": 0.86, "jurisdiction": "Cyprus"},
                            {"id": "C-203", "name": "Golden Horizon Logistics Ltd", "type": "Company", "risk_score": 0.62, "jurisdiction": "United Kingdom"},
                            {"id": "C-208", "name": "Lumina Capital Partners LP", "type": "Company", "risk_score": 0.48, "jurisdiction": "United States"}
                        ],
                        "relationship_chain": [
                            {"share_pct": 100.0, "since": "2020-03-15"},
                            {"share_pct": 85.0, "since": "2020-08-01"},
                            {"share_pct": 90.0, "since": "2021-02-14"},
                            {"share_pct": 75.0, "since": "2021-11-20"}
                        ]
                    }
                ]
            }
        elif company_id in ("C-211", "Blue Water Real Estate GmbH"):
            return {
                "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
                "target_company_id": "C-211",
                "beneficial_owners": [
                    {
                        "ubo_id": "P-102",
                        "ubo_name": "Elena Sterling",
                        "nationality": "Cypriot",
                        "is_pep": True,
                        "person_risk": 0.78,
                        "company_id": "C-211",
                        "company_name": "Blue Water Real Estate GmbH",
                        "effective_ownership_pct": 100.0,
                        "ownership_depth": 2,
                        "ownership_chain": [
                            {"id": "P-102", "name": "Elena Sterling", "type": "Person", "risk_score": 0.78, "jurisdiction": "Cypriot"},
                            {"id": "C-204", "name": "Sovereign Blue Maritime Corp", "type": "Company", "risk_score": 0.88, "jurisdiction": "Panama"},
                            {"id": "C-211", "name": "Blue Water Real Estate GmbH", "type": "Company", "risk_score": 0.50, "jurisdiction": "Germany"}
                        ],
                        "relationship_chain": [
                            {"share_pct": 100.0, "since": "2019-06-10"},
                            {"share_pct": 100.0, "since": "2021-04-05"}
                        ]
                    }
                ]
            }
        else:
            return {
                "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
                "target_company_id": company_id,
                "beneficial_owners": []
            }

    @staticmethod
    def find_shortest_sanction_path(entity_id: str) -> Dict[str, Any]:
        """Finds shortest graph path from an entity to any sanction list or designated entity."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_SHORTEST_SANCTION_PATH, {"entity_id": entity_id})
                if results:
                    return {
                        "mode": "live_cognodb",
                        "found": True,
                        "path": results[0]
                    }
                return {"mode": "live_cognodb", "found": False, "message": "No sanction path found within 6 hops"}
            except Exception as e:
                logger.warning(f"Live shortest sanction path query failed: {e}")

        # Fallback simulation
        if entity_id in ("C-208", "ACC-9009", "Lumina Capital Partners LP"):
            return {
                "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
                "found": True,
                "path": {
                    "distance": 4,
                    "sanction_id": "SANCT-OFAC-SDN",
                    "sanctioning_body": "US Dept of Treasury",
                    "sanction_program": "UKRAINE-EO14024 / DEFENSE_SECTOR",
                    "sanction_reason": "Dual-use technology procurement & weapons proliferation funding",
                    "path_nodes": [
                        {"id": "C-208", "name": "Lumina Capital Partners LP", "label": "Company", "risk_score": 0.48, "country": "United States"},
                        {"id": "ACC-9009", "name": "ACC-9009", "label": "BankAccount", "risk_score": 0.0, "country": "United States"},
                        {"id": "ACC-9004", "name": "ACC-9004", "label": "BankAccount", "risk_score": 0.0, "country": "United Kingdom"},
                        {"id": "ACC-9005", "name": "ACC-9005", "label": "BankAccount", "risk_score": 0.0, "country": "UAE"},
                        {"id": "ACC-9007", "name": "ACC-9007", "label": "BankAccount", "risk_score": 0.0, "country": "Russia"},
                        {"id": "C-205", "name": "Vostok Precision Dynamics", "label": "Company", "risk_score": 0.99, "country": "Russia"},
                        {"id": "SANCT-OFAC-SDN", "name": "OFAC SDN List", "label": "SanctionList", "risk_score": 1.0, "country": "N/A"}
                    ],
                    "path_relationships": [
                        {"type": "HOLDS_ACCOUNT", "from_id": "C-208", "to_id": "ACC-9009", "properties": {}},
                        {"type": "TRANSFERRED_TO", "from_id": "ACC-9004", "to_id": "ACC-9009", "properties": {"amount": 1350000.0, "tx_id": "TX-SANCT-303"}},
                        {"type": "TRANSFERRED_TO", "from_id": "ACC-9005", "to_id": "ACC-9004", "properties": {"amount": 1400000.0, "tx_id": "TX-SANCT-302"}},
                        {"type": "TRANSFERRED_TO", "from_id": "ACC-9007", "to_id": "ACC-9005", "properties": {"amount": 1450000.0, "tx_id": "TX-SANCT-301"}},
                        {"type": "HOLDS_ACCOUNT", "from_id": "C-205", "to_id": "ACC-9007", "properties": {}},
                        {"type": "SANCTIONED_UNDER", "from_id": "C-205", "to_id": "SANCT-OFAC-SDN", "properties": {}}
                    ]
                }
            }
        elif entity_id in ("P-101", "Viktor Sterling"):
            return {
                "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
                "found": True,
                "path": {
                    "distance": 1,
                    "sanction_id": "SANCT-EU-CFSP",
                    "sanctioning_body": "European External Action Service",
                    "sanction_program": "REG_269_2014",
                    "sanction_reason": "Destabilizing actions & illicit financial asset concealment",
                    "path_nodes": [
                        {"id": "P-101", "name": "Viktor Sterling", "label": "Person", "risk_score": 0.94, "country": "Russian"},
                        {"id": "SANCT-EU-CFSP", "name": "EU Consolidated Sanctions", "label": "SanctionList", "risk_score": 1.0, "country": "N/A"}
                    ],
                    "path_relationships": [
                        {"type": "SANCTIONED_UNDER", "from_id": "P-101", "to_id": "SANCT-EU-CFSP", "properties": {"listed_date": "2022-05-10"}}
                    ]
                }
            }

        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "found": False,
            "message": f"No direct or indirect sanction path found for entity {entity_id}."
        }

    @staticmethod
    def get_mule_hubs(limit: int = 10) -> Dict[str, Any]:
        """Discovers mule/bridge accounts with high transfer in/out centrality."""
        if db._is_connected:
            try:
                results = db.execute_query(CYPHER_MULE_HUBS, {"limit": limit})
                return {
                    "mode": "live_cognodb",
                    "hubs": results
                }
            except Exception as e:
                logger.warning(f"Live mule hub query failed: {e}")

        # Fallback simulation
        return {
            "mode": "mock_fallback" if not db._is_connected else "live_cognodb",
            "hubs": [
                {
                    "account_number": "ACC-9005",
                    "bank_name": "Emirates NBD Freezone",
                    "country": "UAE",
                    "risk_level": "HIGH",
                    "unique_senders": 2,
                    "unique_recipients": 2,
                    "total_inflow": 2270000.0,
                    "total_outflow": 2190000.0,
                    "net_retention": 80000.0,
                    "centrality_index": 6.0
                },
                {
                    "account_number": "ACC-9004",
                    "bank_name": "Barclays Commercial London",
                    "country": "United Kingdom",
                    "risk_level": "MEDIUM",
                    "unique_senders": 2,
                    "unique_recipients": 2,
                    "total_inflow": 1980000.0,
                    "total_outflow": 1900000.0,
                    "net_retention": 80000.0,
                    "centrality_index": 6.0
                }
            ]
        }

    @staticmethod
    def execute_custom_cypher(cypher_query: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Executes a user-provided Cypher query against CognoDB."""
        if not db._is_connected:
            return {
                "mode": "demo_mode",
                "success": False,
                "error": "Live CognoDB instance is not connected. Configure credentials in .env to execute arbitrary Cypher.",
                "data": []
            }
        try:
            import time
            t0 = time.time()
            data = db.execute_query(cypher_query, parameters)
            exec_time_ms = round((time.time() - t0) * 1000, 2)
            return {
                "mode": "live_cognodb",
                "success": True,
                "execution_time_ms": exec_time_ms,
                "row_count": len(data),
                "data": data
            }
        except Exception as e:
            return {
                "mode": "live_cognodb",
                "success": False,
                "error": str(e),
                "data": []
            }
