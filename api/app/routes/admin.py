from fastapi import APIRouter, HTTPException
from app.database import db
from app.seed.seed_data import seed_database
from app.config import settings

router = APIRouter(prefix="/api/admin", tags=["System & Administration"])


@router.get("/health")
def get_health_status():
    """Returns the live connection health and driver details."""
    health = db.check_health()
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "database": health,
    }


@router.post("/reconnect")
def reconnect_database():
    """Forces reconnection attempt to CognoDB Cloud using current environment variables."""
    db.close()
    db.initialize()
    return db.check_health()


@router.post("/seed")
def trigger_seed_database(clear_first: bool = True):
    """Triggers dataset ingestion into the live CognoDB instance."""
    if not db._is_connected:
        raise HTTPException(
            status_code=400,
            detail="Cannot seed: Live CognoDB instance is not connected. Check your .env credentials."
        )
    try:
        res = seed_database(clear_first=clear_first)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/clear")
def clear_database():
    """Clears all nodes and relationships from CognoDB."""
    if not db._is_connected:
        raise HTTPException(status_code=400, detail="Database is not connected.")
    try:
        session = db.get_session()
        if session:
            session.run("MATCH (n) DETACH DELETE n")
            session.close()
            return {"success": True, "message": "All nodes and relationships purged from CognoDB."}
        raise HTTPException(status_code=500, detail="Could not acquire session.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
