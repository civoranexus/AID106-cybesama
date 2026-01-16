from fastapi import APIRouter
from routing.router import route_query

router = APIRouter()

@router.post("/query")
def query_router(payload: dict):
    user_query = payload.get("query")
    user_context = payload.get("user_context", {})

    return route_query(user_query, user_context)
