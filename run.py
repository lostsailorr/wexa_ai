"""
Root entrypoint to run SentinelGraph server.
Usage:
    python run.py
"""

import sys
import os
import uvicorn

# Ensure backend/ directory is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "backend")))

from app.config import settings

if __name__ == "__main__":
    port = int(os.getenv("PORT", settings.PORT))
    host = os.getenv("HOST", settings.HOST)
    print(f"\n=======================================================")
    print(f"  Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"  Host: http://{host}:{port}")
    print(f"  API Docs: http://localhost:{port}/docs")
    print(f"=======================================================\n")
    uvicorn.run("app.main:app", host=host, port=port, reload=False)
