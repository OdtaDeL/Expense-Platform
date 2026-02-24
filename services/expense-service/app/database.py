from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./expense.db"
# nếu bạn đang dùng postgres thì giữ nguyên postgres

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # chỉ dùng cho SQLite
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
