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

DATABASE_URL = os.getenv("DATABASE_URL")

# 如果我沒有找到 DATABASE_URL ; 不要繼續跑，直接報錯告訴開發者
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

# 把「DATABASE_URL 有沒有成功載入」這件事情印出來到終端機顯示。
# print("DATABASE_URL loaded:", DATABASE_URL is not None)

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass