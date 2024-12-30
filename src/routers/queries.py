from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Any
from datetime import datetime

router = APIRouter()

# Define Query and QueryResult models
class Query(BaseModel):
    query: str

class QueryResult(BaseModel):
    id: int
    query: str
    timestamp: datetime
    success: bool
    result: Any

class HistoryQuery(BaseModel):  # Only stores query text and metadata
    id: int
    query: str
    timestamp: datetime

# Lists to store run queries and history queries
run_query_result: QueryResult = None  # Stores the most recent query result
history_queries: List[HistoryQuery] = []

# Generate unique IDs for queries
def generate_query_id() -> int:
    return len(history_queries) + 1

@router.post("/api/queries", response_model=QueryResult)
async def run_query(query: Query):
    global run_query_result

    try:
        # Mock result for demonstration purposes
        result = {"mock_key": "mock_value"}
        success = True
    except Exception as e:
        result = str(e)
        success = False

    # Create the QueryResult for the current run
    run_query_result = QueryResult(
        id=generate_query_id(),
        query=query.query,
        timestamp=datetime.now(),
        success=success,
        result=result,
    )

    # Add the query text to history (without result)
    history_queries.append(
        HistoryQuery(
            id=run_query_result.id,
            query=query.query,
            timestamp=run_query_result.timestamp,
        )
    )
    print(f"Added to history: {history_queries}")

    return run_query_result 

@router.get("/api/queries", response_model=List[HistoryQuery])
async def get_history_queries():
    return history_queries

@router.delete("/api/queries/{query_id}", response_model=HistoryQuery)
async def delete_query(query_id: int):
    for query in history_queries:
        if query.id == query_id:
            history_queries.remove(query)
            return query
    raise HTTPException(status_code=404, detail="Query not found")

@router.get("/api/last-query", response_model=QueryResult)
async def get_last_query_result():
    """Fetches the last executed query result."""
    if run_query_result is None:
        raise HTTPException(status_code=404, detail="No query has been executed yet.")
    return run_query_result
