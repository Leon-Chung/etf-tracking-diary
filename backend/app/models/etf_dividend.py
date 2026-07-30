#Python 有命名慣例 : Class 使用 PascalCase（大駝峰）
#變數、函式使用小寫底線 : stock_name 、created_at、get_user()

from datetime import date, datetime
# 從 Python 內建的 datetime 模組，導入 date, datetime 這兩個類別。
from decimal import Decimal
# 從 Python 內建的 decimal 模組裡，導入 Decimal 這個類別。
# Decimal 它是 Python 裡專門處理：精確小數計算

from sqlalchemy import (
  Date,
  DateTime,
  Numeric,
  ForeignKey,
  func
)


from sqlalchemy.orm import Mapped, mapped_column


from app.database import Base


class ETFDividend(Base):

  __tablename__ = 'etf_dividend'

  id: Mapped[int] = mapped_column(primary_key=True)

  etf_id: Mapped[int] = mapped_column(
    ForeignKey(
        "etf_info.id",
        ondelete="CASCADE"
      ),
      nullable=False
    )

  ex_dividend_date: Mapped[date] = mapped_column(Date, nullable=False)

  payment_date: Mapped[date | None] = mapped_column(Date)

  cash_dividend: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)

  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

  

