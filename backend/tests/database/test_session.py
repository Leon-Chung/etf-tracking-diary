# 確認能不能建立 SQLAlchemy Session

from app.database import SessionLocal

def test_create_database_session():
    db = SessionLocal()

    try:
        # assert(確認) 是 Python 關鍵字: 預期 db 不應該是 None
        assert db is not None
    finally:
        db.close()