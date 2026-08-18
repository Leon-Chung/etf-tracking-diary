# FastAPI 是 FastAPI 框架提供的類別（class）
# Depends 是 FastAPI 提供的 Dependency Injection（依賴注入）工具。
from fastapi import FastAPI, Depends

# 從 app.database.py 檔案導入 get_db 這個函式
from app.database import get_db

# 建立一個 FastAPI 應用程式物件，放到 app 裡
app = FastAPI()

#--------Phase 1----------------------------------------

# 確認 FastAPI 本身可以正常運作。
# @app.get("/")
# def home():
#     return {
#         "message": "ETF API is running!"
#     }


#--------Phase 2----------------------------------------

# 透過 Dependency Injection，讓 FastAPI 提供 Database Session 給 API
@app.get("/")

# home() 函式需要 db，FastAPI 透過 Depends(get_db) 執行 get_db()，
# 而 get_db() 再透過 SessionLocal() 建立 Session，
# 最後把這個 Session 注入 home() 的 db。
def home( db=Depends(get_db)):

    # 驗證：每一次 HTTP Request 都會取得一個新的 Database Session
    # print("DB Session:", db)

    return {
        "message": "ETF API is running!"
    }