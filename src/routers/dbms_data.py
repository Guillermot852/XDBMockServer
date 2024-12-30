from fastapi import APIRouter
from typing import List
from src.dbmsData import dbms_data

router = APIRouter()

@router.get("/api/dbms_data", response_model=List[dict])
async def get_dbms_data():
    return dbms_data