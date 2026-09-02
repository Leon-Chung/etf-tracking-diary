
#Python 有命名慣例 : Class 使用 PascalCase（大駝峰）
#變數、函式使用小寫底線 : stock_name 、created_at、get_user()

from datetime import date, datetime #2026.07.27 新增從 Python 內建的 datetime 模組，導入 date 和 datetime 這兩個類別。


from sqlalchemy import String, Date, DateTime, func 
# 這是在拿 PostgreSQL 欄位型別的對應工具。 (VARCHAR、DATE、TIMESTAMP)

from sqlalchemy.orm import Mapped, mapped_column 
# Mapped：建立 Python 與資料庫欄位之間的映射標記
# mapped_column：定義資料庫欄位的詳細規格

from app.database import Base
#把 SQLAlchemy 的基底類別 Base 載入，讓我的資料表 Model 可以繼承它。

class ETFInfo(Base): # 每一張資料表，都會建立一個 Python Class，而且這個 Class 都會繼承同一個 Base。( class 表名稱(Base): )
    __tablename__ = "etf_info" # 這才是與 SQL 建立 對應關係

    id: Mapped[int] = mapped_column( primary_key=True ) #建立資料表的 id 欄位，它是一個整數主鍵，由資料庫管理唯一編號。

    # id : 這是 Python Class 裡面的屬性名稱。
    # Mapped[int] : 這是 Python 的型別註記 + SQLAlchemy ORM 標記 ; int => 代表 Python 資料型別是整數
    # mapped_column(primary_key=True) : 描述資料庫欄位的設定 ; primary_key=True => 這個欄位是主鍵。

    # 對應關係：
        # PostgreSQL                 Python

        # id INTEGER        ←→      id: Mapped[int]

        # PRIMARY KEY       ←→      primary_key=True

    # 那 SQL GENERATED ALWAYS AS IDENTITY 呢？
     #代表 PostgreSQL 自動產生流水號 ; 但在 SQLAlchemy 2.x 中：已經知道這是主鍵，會讓資料庫使用自動生成策略。
 
    symbol: Mapped[str] = mapped_column( String(10), unique=True, nullable=False ) #建立一個叫 symbol 的欄位，它存放最多 10 個字元的文字，而且每一筆 ETF 的 symbol 都不能重複，也不能沒有值。

    # 對應關係：
        # PostgreSQL                 Python

        # VARCHAR(10)        ←→      String(10)
        # UNIQUE             ←→      unique=True
        # NOT NULL           ←→      nullable=False

    # 所以 True / False 可以這樣記:
        # 設定             True               False

        # primary_key ←→  是主鍵         ←→  不是主鍵   
        # unique      ←→  啟用唯一限制    ←→ 不限制重複    
        # nullable    ←→  允許 NULL限    ←→  不允許 NULL

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # 新增 建立第一次 未來 Schema 修改 測試
    description: Mapped[str | None] = mapped_column(
    String(255)
    )

    issuer: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    dividend_frequency: Mapped[str | None] = mapped_column(
        String(20)
    )

    # listing_date: Mapped[Date | None] = mapped_column( Date ) # 優化前

    listing_date: Mapped[date | None] = mapped_column( Date ) # Mapped[...] 使用 Python 型別；mapped_column(...) 使用 SQLAlchemy 資料庫型別。

      # Mapped[date | None]：告訴 Python，這個屬性是一個 date 或 None
      # mapped_column(Date)：告訴 SQLAlchemy，資料庫欄位型別是 DATE

    # created_at: Mapped[DateTime] = mapped_column( DateTime ) # 優化前

    created_at: Mapped[datetime] = mapped_column( # Mapped[...] 使用 Python 型別；mapped_column(...) 使用 SQLAlchemy 資料庫型別。 
        DateTime, # 資料庫欄位型別
        server_default=func.now(), 
        # 如果沒有提供 created_at，就由 PostgreSQL 自己填入現在時間。
        # func: SQLAlchemy 提供的一個工具，讓 Python 可以呼叫 PostgreSQL 執行 NOW() 函式，取得目前的時間。
        nullable=False # 這個欄位不能是空的（NULL）。
        ) 