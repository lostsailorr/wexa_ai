from fastapi import APIRouter, Query, Body
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.services.graph_service import GraphService

router = APIRouter(prefix="/api/analytics", tags=["Graph Analytics & Intelligence"])


class CypherExecutionRequest(BaseModel):
    query: str
    parameters: Optional[Dict[str, Any]] = None


@router.get("/circular-rings")
def get_circular_rings(limit: int = Query(10, ge=1, le=50)):
    """Detects circular transaction rings (smurfing/layering loops of 3-6 hops)."""
    return GraphService.detect_circular_rings(limit=limit)


@router.get("/ubo/{company_id}")
def resolve_ubo(
    company_id: str,
    min_share_pct: float = Query(10.0, ge=1.0, le=100.0, description="Minimum effective ownership percentage")
):
    """Recursively computes multi-tier Ultimate Beneficial Ownership (UBO) paths."""
    return GraphService.resolve_ubo(company_id=company_id, min_share_pct=min_share_pct)


@router.get("/shortest-sanction-path/{entity_id}")
def get_shortest_sanction_path(entity_id: str):
    """Finds the shortest network path connecting an entity to any sanctioned node."""
    return GraphService.find_shortest_sanction_path(entity_id=entity_id)


@router.get("/mule-hubs")
def get_mule_hubs(limit: int = Query(10, ge=1, le=50)):
    """Discovers high-centrality intermediary and mule accounts."""
    return GraphService.get_mule_hubs(limit=limit)


@router.post("/cypher-console")
def run_custom_cypher(payload: CypherExecutionRequest):
    """Executes arbitrary Cypher queries directly against CognoDB Cloud."""
    return GraphService.execute_custom_cypher(cypher_query=payload.query, parameters=payload.parameters)
