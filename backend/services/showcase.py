from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database import db_session
from backend.entities.showcase_entity import ShowcaseProjectEntity

from ..models.showcase import ShowcaseProject


class ShowcaseService:
    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    # Get all showcases
    def get_showcases(self) -> list[ShowcaseProject]:
        query = select(ShowcaseProjectEntity)
        showcase_entities = self._session.scalars(query).all()

        return [entity.to_model() for entity in showcase_entities]
