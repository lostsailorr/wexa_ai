from fastapi import APIRouter, Query
from typing import Optional
from app.services.graph_service import GraphService

router = APIRouter(prefix="/api/graph", tags=["Graph Operations"])


@router.get("/subgraph")
def get_subgraph(
    node_type: Optional[str] = Query(None, description="Filter by node label (e.g. Person, Company, BankAccount)"),
    min_risk: Optional[float] = Query(None, description="Filter by minimum risk score (0.0 to 1.0)")
):
    """Retrieves full or filtered network graph for visual canvas rendering."""
    return GraphService.get_subgraph(node_type=node_type, min_risk=min_risk)


@router.get("/neighborhood/{entity_id}")
def get_neighborhood(entity_id: str):
    """Retrieves 1-2 hop neighborhood surrounding a selected entity."""
    return GraphService.get_entity_neighborhood(entity_id=entity_id)


@router.get("/metrics")
def get_metrics():
    """Returns real-time aggregate statistics for nodes and relationships."""
    return GraphService.get_summary_metrics()
