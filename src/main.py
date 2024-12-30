from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.health import router as health_router
from src.routers.db_config import router as db_config_router
from src.routers.dbms_data import router as dbms_data_router
from src.routers.queries import router as queries_router

app = FastAPI()

# Allow CORS from any source
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(health_router)
app.include_router(db_config_router)
app.include_router(dbms_data_router)
app.include_router(queries_router)