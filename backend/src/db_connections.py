from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db_session_factory(
    db_url: str, 
    connect_args: dict[str, Any],   
):
    engine = create_engine(
        db_url, connect_args=connect_args,
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_session():
        db = SessionLocal()

        try:
            yield db
        finally:
            db.close()

    return get_session

