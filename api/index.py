import os
import sys
import traceback

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(root_dir, "backend")

for path in [current_dir, backend_dir, root_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

try:
    from app.main import app
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()
    err_trace = traceback.format_exc()
    
    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    async def catch_all(full_path: str):
        return JSONResponse(
            status_code=500,
            content={"status": "error", "error": "FastAPI Initialization Failed", "traceback": err_trace}
        )
