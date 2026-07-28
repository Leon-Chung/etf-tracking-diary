#Python 有命名慣例 : Class 使用 PascalCase（大駝峰）
#變數、函式使用小寫底線 : stock_name 、created_at、get_user()

from datetime import date, datetime
# 從 Python 內建的 datetime 模組，導入 date 和 datetime 這兩個類別。

from decimal import Decimal
# 從 Python 內建的 decimal 模組裡，導入 Decimal 這個類別。
# Decimal 它是 Python 裡專門處理：精確小數計算

from sqlalchemy import (
    Integer,
    Date,
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

class ETFSnapshot(Base): # 每一張資料表，都會建立一個 Python Class，而且這個 Class 都會繼承同一個 Base。( class 表名稱(Base): )

    __tablename__ = "etf_snapshot" # 這才是與 SQL 建立 對應關係

    id: Mapped[int] = mapped_column( primary_key=True )

    etf_id: Mapped[int] = mapped_column( ForeignKey("etf_info.id" , ondelete="CASCADE"), nullable=False )
    # ForeignKey : 這個欄位是外部表的資料。
    # ForeignKey 是對應到 SQL 的 這一段: 
    # CONSTRAINT fk_snapshot_etf
      # FOREIGN KEY (etf_id) : etf_snapshot 這張表裡面的 etf_id 是一個外部鍵。
      # REFERENCES etf_info(id) : etf_id 要參考 etf_info 表的 id 欄位。
      # ON DELETE CASCADE, : 如果父資料被刪除，相關子資料一起刪除。

    snapshot_date: Mapped[date] = mapped_column( Date, nullable=False )

    fund_size: Mapped[Decimal | None] = mapped_column(
        
      Numeric(18,2)
      # 數字，小數最多兩位。
    )

    beneficiaries: Mapped[int | None] = mapped_column(

      Integer
      # 儲存「整數」
    )

    management_fee: Mapped[Decimal | None] = mapped_column(

      Numeric(5,2)
      # 總共最多 5 位數，其中 2 位小數。
    )

    nav: Mapped[Decimal | None] = mapped_column(

      Numeric(10,2)
      # 總共 10 位數，小數 2 位。
    )

    created_at: Mapped[datetime] = mapped_column( # Mapped[...] 使用 Python 型別；mapped_column(...) 使用 SQLAlchemy 資料庫型別。 
            
      DateTime, # 資料庫欄位型別
            
      server_default=func.now(), 
        # 如果沒有提供 created_at，就由 PostgreSQL 自己填入現在時間。
        # func: SQLAlchemy 提供的一個工具，讓 Python 可以呼叫 PostgreSQL 執行 NOW() 函式，取得目前的時間。
      
      nullable=False # 這個欄位不能是空的（NULL）。
    )

    __table_args__ = ( # __table_args__ 是 SQLAlchemy 特殊保留名稱 => 放「資料表層級設定」。
        UniqueConstraint( # UniqueConstraint : 多個欄位的規則，建立唯一限制( 這兩個一起唯一 => etf_id + snapshot_date)。 
            "etf_id",
            "snapshot_date",
            name="uq_snapshot" # 這是給這個限制取名字。
        ),

    # __table_args__ 是對應到 SQL 的 這一段:
      # CONSTRAINT uq_snapshot => 對應 name="uq_snapshot"
        # UNIQUE(etf_id, snapshot_date) // 限制 etf_id + snapshot_date 這兩個欄位組合起來不能重複。    
    
    ) 