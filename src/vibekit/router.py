from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/vibekit", tags=["vibekit"])


class InfoResponse(BaseModel):
    status: str


@router.get("/info")
def info() -> InfoResponse:
    return InfoResponse(status="✅")
