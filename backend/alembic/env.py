from logging.config import fileConfig

# 讓 Alembic 直接使用 database.py 已經建立好的 engine，這以下兩個就不需要了。
# from sqlalchemy import engine_from_config
# from sqlalchemy import pool



from alembic import context

# 導入 app.database 拿到 SQLAlchemy 已建立的 Base.metadata 以及 DB connection
from app.database import Base, engine, DATABASE_URL
# 導入 app.models 確保你的 models/__init__.py 內 5 個 Model 被載入、註冊進 Base.metadata; 然後：Base.metadata 才會有初始的 5 張 Table
import app.models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

#這裡不能維持 None，要讓 Alembic 知道你的 SQLAlchemy Metadata。
# target_metadata = None

# 目前 Base.metadata 應該有 初始的 5 張 Table Model; 並告訴 Alembic：「我要拿這份 Metadata 跟 PostgreSQL Schema 比對」
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # 目前 database.py 已經有 Database URL 來源 ; 所以 Alembic 不需要自己再讀一次
    # url = config.get_main_option("sqlalchemy.url")

    # 直接透過 from app.database import Base, engine, DATABASE_URL 來導入讀取
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # 以下那一段是告訴 Alembic：「你自己去 alembic.ini 找資料庫設定，然後自己建立 Engine。」
    # connectable = engine_from_config(
    #     config.get_section(config.config_ini_section, {}),
    #     prefix="sqlalchemy.",
    #     poolclass= pool.NullPool,
    # )

    # 但你的專案已經有：database.py 檔案內的 engine ; 所以這裡沒必要再建立第二個 Engine。
    # with connectable.connect() as connection:

    with engine.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
