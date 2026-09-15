# # 把 SQLAlchemy 的 Session 型別拿進來。
# from sqlalchemy.orm import Session

# # 讓 Repository 知道「ETF 資料長什麼樣子」。
# from app.models.etf_info import ETFInfo

# # 建立一個叫 create_etf 的函式，它需要一個 Database Session，以及一個 ETFInfo 物件，最後會回傳一個 ETFInfo。
# def create_etf(db: Session, etf: ETFInfo) -> ETFInfo:
    
#     # 把這個 ETF 交給 SQLAlchemy，準備新增。
#     db.add(etf)
#     # 正式提交這次資料庫變更。
#     db.commit()
#     # 重新從資料庫把這筆資料最新的內容拿回來。
#     db.refresh(etf)

#     return etf