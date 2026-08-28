from fastapi import APIRouter, Query
from app.services.mock_data import MOCK_NODES
from app.database import db

router = APIRouter(prefix="/api/search", tags=["Search & Lookup"])


@router.get("/")
def search_entities(q: str = Query(..., min_length=1, description="Search term for names, account numbers, or IDs")):
    """Searches across Person, Company, BankAccount, and Sanction nodes."""
    search_term = q.strip().lower()
    
    if db._is_connected:
        try:
            cypher = """
            MATCH (n)
            WHERE toLower(coalesce(n.name, '')) CONTAINS $term
               OR toLower(coalesce(n.id, '')) CONTAINS $term
               OR toLower(coalesce(n.account_number, '')) CONTAINS $term
            RETURN
                coalesce(n.id, n.account_number) AS id,
                labels(n)[0] AS label,
                coalesce(n.name, n.account_number) AS name,
                coalesce(n.risk_score, n.base_risk, 0.0) AS risk_score,
                coalesce(n.jurisdiction, n.nationality, n.country, 'N/A') AS country
            LIMIT 15
            """
            results = db.execute_query(cypher, {"term": search_term})
            return {"results": results}
        except Exception:
            pass

    # Fallback search
    matches = []
    for n in MOCK_NODES:
        name = str(n.get("name", "")).lower()
        nid = str(n.get("id", "")).lower()
        acc = str(n.get("account_number", "")).lower()
        if search_term in name or search_term in nid or search_term in acc:
            matches.append({
                "id": n.get("account_number") or n["id"],
                "label": n["label"],
                "name": n.get("name") or n.get("account_number"),
                "risk_score": n.get("risk_score") or n.get("base_risk") or 0.0,
                "country": n.get("jurisdiction") or n.get("nationality") or n.get("country") or "N/A"
            })
    return {"results": matches[:15]}
