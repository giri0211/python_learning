from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

SQLALCHECMY_DATABASE_URL = "sqllite://events.db"

engine =  create_engine(
    SQLALCHECMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)
    
SessionLocal =  sessionmaker(bind=engine)