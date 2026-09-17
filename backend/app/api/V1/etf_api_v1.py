from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.etf_schemas import ETFInfoResponse
from app.services.etf_service_search import ETFService

router = APIRouter(prefix="/api/v1/etf", tags=["ETF 搜尋"])

def get_etf_service() -> ETFService:
    return ETFService()

@router.get("/search", response_model=ETFInfoResponse, summary="搜尋 ETF 基本資訊")
async def search_etf(
    symbol: str,
    service: ETFService = Depends(get_etf_service)
):
    try:
        data = await service.search_etf(symbol=symbol)
        return data
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"內部伺服器錯誤: {str(e)}"
        )