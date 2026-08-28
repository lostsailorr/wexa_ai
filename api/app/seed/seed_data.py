"""
Database Seeding Script for CognoDB Cloud.
Usage:
    python backend/app/seed/seed_data.py
Or invoke via the SentinelGraph web API / Admin panel.
"""

import sys
import os
import logging

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.config import settings
from app.database import db
from app.services.mock_data import MOCK_NODES, MOCK_EDGES

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("sentinelgraph.seeder")


def seed_database(clear_first: bool = True) -> dict:
    """Seeds CognoDB with the SentinelGraph realistic dataset."""
    db.initialize()
    if not db._is_connected:
        raise ConnectionError(f"Cannot seed CognoDB: {db._last_error}")

    session = db.get_session()
    if not session:
        raise ConnectionError("Database session could not be acquired.")

    try:
        if clear_first:
            logger.info("Clearing existing nodes and relationships from CognoDB...")
            session.run("MATCH (n) DETACH DELETE n")

        # 1. Create Constraints / Indexes for high-performance lookups
        logger.info("Creating constraints and indexes...")
        index_queries = [
            "CREATE CONSTRAINT person_id_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.id IS UNIQUE",
            "CREATE CONSTRAINT company_id_unique IF NOT EXISTS FOR (c:Company) REQUIRE c.id IS UNIQUE",
            "CREATE CONSTRAINT bank_account_unique IF NOT EXISTS FOR (b:BankAccount) REQUIRE b.account_number IS UNIQUE",
            "CREATE CONSTRAINT sanction_id_unique IF NOT EXISTS FOR (s:SanctionList) REQUIRE s.id IS UNIQUE",
            "CREATE CONSTRAINT jurisdiction_code_unique IF NOT EXISTS FOR (j:Jurisdiction) REQUIRE j.code IS UNIQUE",
        ]
        for q in index_queries:
            try:
                session.run(q)
            except Exception as ex:
                logger.warning(f"Index creation notice: {ex}")

        # 2. Ingest Nodes
        logger.info(f"Ingesting {len(MOCK_NODES)} nodes into CognoDB...")
        node_counts = {}
        for node in MOCK_NODES:
            label = node["label"]
            props = {k: v for k, v in node.items() if k != "label"}
            
            # Use parameterized Cypher MERGE statement
            if label == "BankAccount":
                query = f"""
                MERGE (n:{label} {{account_number: $account_number}})
                SET n += $props
                """
                session.run(query, {"account_number": props.get("account_number", props.get("id")), "props": props})
            else:
                query = f"""
                MERGE (n:{label} {{id: $id}})
                SET n += $props
                """
                session.run(query, {"id": props["id"], "props": props})
                
            node_counts[label] = node_counts.get(label, 0) + 1

        # 3. Ingest Relationships
        logger.info(f"Ingesting {len(MOCK_EDGES)} relationships into CognoDB...")
        rel_counts = {}
        for edge in MOCK_EDGES:
            rel_type = edge["type"]
            src = edge["source"]
            tgt = edge["target"]
            props = edge.get("properties", {})

            # Parameterized match query linking source and target by id or account_number
            query = f"""
            MATCH (a) WHERE a.id = $src OR a.account_number = $src
            MATCH (b) WHERE b.id = $tgt OR b.account_number = $tgt
            MERGE (a)-[r:{rel_type}]->(b)
            SET r += $props
            """
            session.run(query, {"src": src, "tgt": tgt, "props": props})
            rel_counts[rel_type] = rel_counts.get(rel_type, 0) + 1

        logger.info("Database seeding completed successfully!")
        return {
            "success": True,
            "nodes_inserted": len(MOCK_NODES),
            "relationships_inserted": len(MOCK_EDGES),
            "node_breakdown": node_counts,
            "relationship_breakdown": rel_counts,
        }
    finally:
        session.close()


if __name__ == "__main__":
    print("\n=======================================================")
    print("  SentinelGraph - CognoDB Seeder Utility")
    print(f"  Target URI: {settings.COGNODB_URI}")
    print("=======================================================\n")
    try:
        result = seed_database(clear_first=True)
        print("\n Seeding Summary:")
        print(f"  - Total Nodes: {result['nodes_inserted']}")
        print(f"  - Total Edges: {result['relationships_inserted']}")
        for k, v in result['node_breakdown'].items():
            print(f"     * {k}: {v}")
        print("\nReady for queries and visualization!\n")
    except Exception as e:
        print(f"\n Error seeding database: {e}")
        sys.exit(1)
