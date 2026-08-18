# 確認 engine 能不能真的連到 PostgreSQL。

from app.database import engine


try:
    with engine.connect() as connection:
        print("✅ PostgreSQL 連線成功")

except Exception as e:
    print("❌ PostgreSQL 連線失敗")
    print(e)