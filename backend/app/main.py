# FastAPI 是 FastAPI 框架提供的類別（class）
# Depends 是 FastAPI 提供的 Dependency Injection（依賴注入）工具。
from fastapi import FastAPI, Depends

# 從 app.database.py 檔案導入 get_db 這個函式
from app.database import get_db

# 引入你的 API Router（請確認資料夾是 V1 還是 v1）
from app.api.V1.etf_api_v1 import router as etf_router


# 2. 建立唯一的 FastAPI 應用程式實例 (只建立一次！)
app = FastAPI(
    title="ETF 搜尋服務",
    description="提供 ETF 即時搜尋與保存服務",
    version="1.0.0"
)


# 3. 註冊 ETF 搜尋的 Router
app.include_router(etf_router)


# 4. 根目錄測試 API (Phase 2: 測試 DB 連線 Session)
@app.get("/", summary="健康檢查與 DB 連線測試")
def home(db=Depends(get_db)):
    return {
        "status": "success",
        "message": "ETF API is running!",
        "db_session": str(db)
    }


# ----------------------2026.09.18-old data------------------------------------------------
# 建立一個 FastAPI 應用程式物件，放到 app 裡
# app = FastAPI()

#--------Phase 1----------------------------------------

# 確認 FastAPI 本身可以正常運作。
# @app.get("/")
# def home():
#     return {
#         "message": "ETF API is running!"
#     }


#--------Phase 2----------------------------------------

# 透過 Dependency Injection，讓 FastAPI 提供 Database Session 給 API
# @app.get("/")

# home() 函式需要 db，FastAPI 透過 Depends(get_db) 執行 get_db()，
# 而 get_db() 再透過 SessionLocal() 建立 Session，
# 最後把這個 Session 注入 home() 的 db。
# def home( db=Depends(get_db)):

#     # 驗證：每一次 HTTP Request 都會取得一個新的 Database Session
#     # print("DB Session:", db)

#     return {
#         "message": "ETF API is running!"
#     }