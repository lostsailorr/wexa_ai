import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(root_dir, "backend")

for path in [current_dir, backend_dir, root_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

from fastapi import FastAPI
from app.main import app as _app

# Top-level FastAPI instance variable for Vercel AST parser
app: FastAPI = _app
