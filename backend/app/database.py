# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "postgresql://postgres:konts12345@localhost:5432/etf_database"


# engine = create_engine(DATABASE_URL)


# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )


# Base = declarative_base()  # 這個 Base 就是所有 Model 的父類別。

# Base 是 SQLAlchemy ORM 的基底類別
# 所有資料表 Model 都需要繼承 Base
# 例如：class ETFInfo(Base)

# ---------------------------------------------------------
# SQLAlchemy 2.x 的寫法
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# 從 dotenv 這個套件裡，把 load_dotenv 這個函式拿進來，讓我的 Python 程式可以使用它。
from dotenv import load_dotenv

# os 是 Python 內建的標準函式庫。我們這裡需要它，是因為它可以讓 Python 讀取「環境變數」。
import os

# 去找 .env，把裡面的環境變數讀進來
load_dotenv()

# 按照大型／正式專案的做法，我們不應該把密碼直接寫在 Python 程式碼裡。
# DATABASE_URL = "postgresql://postgres:konts12345@localhost:5432/etf_database"

## 從環境變數取得 Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# 如果我沒有找到 DATABASE_URL ; 不要繼續跑，直接報錯告訴開發者
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

# 把「DATABASE_URL 有沒有成功載入」這件事情印出來到終端機顯示。
# print("DATABASE_URL loaded:", DATABASE_URL is not None)


# 負責管理與 PostgreSQL 的連線
engine = create_engine(DATABASE_URL)

# 負責建立每一次 Database 操作所需要的 Session
SessionLocal = sessionmaker(
    #建立出來的 Session，要使用這個 Engine 去連資料庫
    bind=engine,
    #不要讓 SQLAlchemy 自動幫我們 flush
    autoflush=False,
    #不要自動幫我 Commit。
    autocommit=False,
)

#  所有 ORM Model 都應該繼承這個 Base
class Base(DeclarativeBase):
    pass


# def 是 Python 用來**定義函式（function）**的關鍵字。
# 建立一個叫做 get_db 的函式。
# 冒號代表： 接下來縮排的內容，就是這個函式要執行的程式。
def get_db():
    # 呼叫 SessionLocal，建立一個 Database Session，並把這個 Session 指派給變數 db
    db = SessionLocal()

    # 嘗試執行
    try:
        # yield 是 Python 關鍵字: 用來建立/控制 Generator（生成器），遇到 yield 時先把這個值交出去，之後可以從這裡繼續。
        yield db
        
    # 不管怎樣都執行
    finally:
        # 使用完關閉 Session
        db.close()