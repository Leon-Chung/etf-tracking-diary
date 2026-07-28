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


DATABASE_URL = "postgresql://postgres:konts12345@localhost:5432/etf_database"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass