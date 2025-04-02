from fastapi import APIRouter
from app.routes import todo

router = APIRouter(prefix="/api")
router.include_router(todo.router, prefix="/todos", tags=["todos"])