from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Any, Optional
from datetime import datetime

router = APIRouter()

# Define Query and QueryResult models
class Query(BaseModel):
    id: int
    query: str
    timestamp: datetime

class QueryResult(BaseModel):
    id: int
    query: str
    timestamp: datetime
    result: Any

class HistoryQuery(BaseModel):  # Stores query text and metadata
    id: int
    query: str
    timestamp: datetime
    success: bool


# List to store history and a single variable for the last query result
history_queries: List[HistoryQuery] = []
last_query_result: Optional[QueryResult] = None

# Generate unique IDs for queries
def generate_query_id() -> int:
    return len(history_queries) + 1

@router.post("/api/queries", response_model=QueryResult)
async def run_query(query: Query):
    print(f"Received request: {query}")

    try:
        # Mock execution of the query
        result = {"mock_key": "mock_value"}  # Replace with real execution logic
        success = True
    except Exception as e:
        result = str(e)
        success = False

    # Create the QueryResult for the current run
    query_result = QueryResult(
        id=query.id,
        query=query.query,
        timestamp=query.timestamp,
        success=success,
        result=result,
    )

    # Add to history and update the last query result
    history_queries.append(
        HistoryQuery(
            id=query_result.id,
            query=query.query,
            timestamp=query_result.timestamp,
            success=success,
        )
    )
    last_query_result = query_result

    print(f"Query executed and added to history: {query_result}")
    return query_result


@router.get("/api/queries", response_model=List[HistoryQuery])
async def get_history_queries():
    """Fetches all past queries (without results)."""
    return history_queries

@router.get("/api/last-query", response_model=QueryResult)
async def get_last_query_result():
    """Fetches the most recent executed query result."""
    if last_query_result is None:
        raise HTTPException(status_code=404, detail="No query has been executed yet.")
    return last_query_result

@router.delete("/api/queries/{query_id}", response_model=HistoryQuery)
async def delete_query(query_id: int):
    """
    Deletes a query from history. Does not affect the last query result.
    """
    for query in history_queries:
        if query.id == query_id:
            history_queries.remove(query)
            return query
    raise HTTPException(status_code=404, detail="Query not found")
