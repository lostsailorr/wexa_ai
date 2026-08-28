import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure backend/ is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/admin/health")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "database" in data
    assert "status" in data["database"]


def test_graph_metrics_endpoint():
    response = client.get("/api/graph/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "metrics" in data
    metrics = data["metrics"]
    assert metrics["total_nodes"] > 0
    assert metrics["total_relationships"] > 0


def test_subgraph_endpoint():
    response = client.get("/api/graph/subgraph")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "edges" in data
    assert len(data["nodes"]) > 0


def test_circular_rings_endpoint():
    response = client.get("/api/analytics/circular-rings?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "rings" in data
    assert len(data["rings"]) > 0
    first_ring = data["rings"][0]
    assert first_ring["loop_length"] >= 3
    assert first_ring["total_volume"] > 0


def test_ubo_resolution_endpoint():
    response = client.get("/api/analytics/ubo/C-208")
    assert response.status_code == 200
    data = response.json()
    assert "beneficial_owners" in data
    assert len(data["beneficial_owners"]) > 0
    first_ubo = data["beneficial_owners"][0]
    assert first_ubo["effective_ownership_pct"] > 0
    assert first_ubo["ownership_depth"] >= 2


def test_shortest_sanction_path_endpoint():
    response = client.get("/api/analytics/shortest-sanction-path/C-208")
    assert response.status_code == 200
    data = response.json()
    assert data["found"] is True
    assert data["path"]["distance"] > 0
    assert len(data["path"]["path_nodes"]) > 0


def test_search_endpoint():
    response = client.get("/api/search/?q=Sterling")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0
