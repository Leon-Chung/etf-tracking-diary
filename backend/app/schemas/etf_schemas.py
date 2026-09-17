from pydantic import BaseModel, Field

class ETFInfoResponse(BaseModel):
    symbol: str = Field(..., description="ETF 代碼，例如 0052")
    name: str = Field(..., description="ETF 名稱，例如 富邦科技")
    issuer: str = Field(..., description="發行券商，例如 元大投信, 富邦投信")