from abc import ABC, abstractmethod
from typing import Optional
from app.schemas.etf_schemas import ETFInfoResponse

class BaseETFCrawler(ABC):
    @property
    @abstractmethod
    def issuer_name(self) -> str:
        """券商名稱"""
        pass

    @abstractmethod
    async def fetch_etf_info(self, symbol: str) -> Optional[ETFInfoResponse]:
        """
        根據 ETF 代碼抓取資料
        如果該券商查無此 ETF，回傳 None
        """
        pass