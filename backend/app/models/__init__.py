# 建立 Model Registry（模型註冊中心）

# 第 1 步：加入全部 Model

#來自 .(目前資料夾的 models/ ) etf_price_history.py 檔案內的 class ETFPriceHistory 載入
from .etf_price_history import ETFPriceHistory

from .etf_info import ETFInfo

from .etf_snapshot import ETFSnapshot

from .etf_holdings import ETFHolding

from .etf_dividend import ETFDividend

# 使用 ALL 集中匯入

__all__ = [
  "ETFPriceHistory",
  "ETFInfo",
  "ETFSnapshot",
  "ETFHolding",
  "ETFDividend"
]