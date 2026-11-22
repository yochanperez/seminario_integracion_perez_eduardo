from fastapi import FastAPI
from src.routers.hello_world import router as hello_router
from src.routers.task_router import tasks_router

app = FastAPI(title="Proyecto FastAPI - Seminario de Integración")

app.include_router(hello_router, tags=["Hello World"])
app.include_router(tasks_router, tags=["Tasks"])
