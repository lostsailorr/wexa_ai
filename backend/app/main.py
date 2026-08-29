import os
import sys

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.database import db
from app.routes import graph, analytics, search, admin

# Setup Logging
logging.basicConfig(
    level=logging.INFO if not settings.DEBUG else logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("sentinelgraph")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize CognoDB driver
    logger.info("Initializing SentinelGraph application...")
    db.initialize()
    yield
    # Shutdown: Close driver
    logger.info("Shutting down SentinelGraph and closing CognoDB connection...")
    db.close()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Anti-Money Laundering (AML), Sanctions Evasion & UBO Graph Intelligence Platform backed by CognoDB Cloud."
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(graph.router)
app.include_router(analytics.router)
app.include_router(search.router)
app.include_router(admin.router)

@app.get("/api/health")
def api_health_check():
    return {"status": "healthy", "service": settings.APP_NAME}

@app.get("/api")
def api_root_check():
    return {"status": "healthy", "service": settings.APP_NAME}


# Mount Static Files (Frontend)
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/")
    async def serve_index():
        return FileResponse(os.path.join(static_dir, "index.html"))
else:
    @app.get("/")
    async def root():
        return {
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "message": "Backend API operational."
        }
