from fastapi import APIRouter
from schemas.info import InfoResponse

router = APIRouter()

@router.get("/pm-kisan", response_model=InfoResponse)
def pm_kisan_info():
    return InfoResponse(
        success=True,
        message="Information fetched successfully",
        source="database",
        title="PM Kisan Samman Nidhi",
        summary="A government scheme providing income support to farmers.",
        details="Eligible farmers receive ₹6,000 per year in three installments."
    )
