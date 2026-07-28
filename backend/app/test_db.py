from database import engine


try:
    with engine.connect() as connection:
        print("✅ PostgreSQL 連線成功")

except Exception as e:
    print("❌ PostgreSQL 連線失敗")
    print(e)