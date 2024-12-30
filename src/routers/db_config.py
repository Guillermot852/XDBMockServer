import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

router = APIRouter()

class Nodes(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    hostName: str
    dbPort: int
    dbName: str
    dbType: str
    dbUser: str
    dbPassword: str
    dbRootUser: str
    dbRootPassword: str

nodes_list = []

@router.post("/api/topology/nodes", response_model=Nodes)
async def create_node(node: Nodes):
    nodes_list.append(node)
    return node

@router.get("/api/topology/nodes", response_model=List[Nodes])
async def get_nodes():
    return nodes_list

@router.get("/api/topology/nodes/{id}", response_model=Nodes)
async def get_node(id: str):
    for node in nodes_list:
        if node.id == id:
            return node
    raise HTTPException(status_code=404, detail="Node not found")

@router.put("/api/topology/nodes/{id}", response_model=Nodes)
async def update_node(id: str, updated_node: Nodes):
    for index, node in enumerate(nodes_list):
        if node.id == id:
            nodes_list[index] = updated_node
            return updated_node
    raise HTTPException(status_code=404, detail="Node not found")

@router.delete("/api/topology/nodes/{id}", response_model=Nodes)
async def delete_node(id: str):
    for index, node in enumerate(nodes_list):
        if node.id == id:
            deleted_node = nodes_list.pop(index)
            return deleted_node
    raise HTTPException(status_code=404, detail="Node not found")