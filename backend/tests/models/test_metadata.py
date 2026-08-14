# 測試「Model 有沒有註冊到 Base.metadata」

from app.database import Base

# 將 app/models/__init__.py 集中匯入的檔案, 匯入過來測試
import app.models

def test_models_registered_in_metadata():

    # 把 SQLAlchemy Metadata 裡面目前知道的資料表拿出來。
    tables = Base.metadata.tables 

    # 然後我們檢查： etf_info 有沒有在裡面？
    assert "etf_info" in tables
    assert "etf_snapshot" in tables
    assert "etf_holdings" in tables
    assert "etf_dividend" in tables
    assert "etf_price_history" in tables