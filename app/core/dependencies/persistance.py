from typing import Generator

from fastapi import Depends
from sqlmodel import Session

from app.core.db_config import DB_ENGINE
from app.persistence.common import GroupPersistence
from app.persistence.postgress import PostgresGroupPersistence


def session_dependecy() -> Generator[Session, None, None]:
    with Session(DB_ENGINE) as session:
        yield session

def group_persistence_dependency(session: Session = Depends(session_dependecy)) -> GroupPersistence:
    return PostgresGroupPersistence(session=session)