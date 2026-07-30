

from datetime import date, datetime

from decimal import Decimal


from sqlalchemy import (
  Date,
  DateTime,
  Numeric,
  ForeignKey,
  UniqueConstraint,
  func
)

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class ETFPriceHistory(Base):

  __tablename__ = "etf_price_history"

  id: Mapped[int] = mapped_column(
    primary_key=True
  )

  etf_id: Mapped[int] = mapped_column(
    ForeignKey(
        "etf_info.id",
        ondelete="CASCADE"
    ),
    nullable=False
  )

  price_date: Mapped[date] = mapped_column(
    Date,
    nullable=False
  )

  close_price: Mapped[Decimal | None] = mapped_column(
    Numeric(10,2)
  )

  created_at: Mapped[datetime] = mapped_column(
    DateTime,
    server_default=func.now(),
    nullable=False
  )

  __table_args__ = (
    UniqueConstraint(
      "etf_id",
      "price_date",
      name="uq_price"
    ),
  )