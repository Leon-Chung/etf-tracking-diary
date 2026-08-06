#Python 有命名慣例 : Class 使用 PascalCase（大駝峰）
#變數、函式使用小寫底線 : stock_name 、created_at、get_user()

from datetime import datetime
# 從 Python 內建的 datetime 模組，導入 datetime 這類別。
from decimal import Decimal
# 從 Python 內建的 decimal 模組裡，導入 Decimal 這個類別。
# Decimal 它是 Python 裡專門處理：精確小數計算

from sqlalchemy import (
      String,
      SmallInteger,
      DateTime,
      Numeric,
      ForeignKey,
      UniqueConstraint,
      func
)

# 拿 PostgreSQL 欄位型別的對應工具。 (VARCHAR、DATE、TIMESTAMP)

from sqlalchemy.orm import Mapped, mapped_column
# Mapped：建立 Python 與資料庫欄位之間的映射標記
# mapped_column：定義資料庫欄位的詳細規格

from app.database import Base
#把 SQLAlchemy 的基底類別 Base 載入，讓我的資料表 Model 可以繼承它。

class ETFHolding(Base):

  __tablename__ = 'etf_holdings'

  id: Mapped[int] = mapped_column(primary_key=True)

  snapshot_id: Mapped[int] = mapped_column(ForeignKey("etf_snapshot.id", ondelete='CASCADE'), nullable=False)

  rank: Mapped[int] = mapped_column(SmallInteger, nullable=False)

  stock_symbol: Mapped[str] = mapped_column(String(10), nullable=False)

  stock_name: Mapped[str] = mapped_column(String(100), nullable=False)

  weight: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)

  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

  __table_args__ = (
    UniqueConstraint(
      'snapshot_id', 
      'rank',
       name='uq_holding_rank'
    ),
  )