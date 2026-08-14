
# 測試「app.Model檔案夾內的 table 能不能被載入」

# 從 models/etf_info.py 找 class ETFPriceHistory, class ETFInfo ... 依此類推
from app.models import (
  ETFPriceHistory,
  ETFInfo,
  ETFSnapshot,
  ETFHolding,
  ETFDividend
)

print(ETFPriceHistory)
print(ETFInfo)
print(ETFSnapshot)
print(ETFHolding)
print(ETFDividend)