from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database import db_session
from backend.entities.showcase_entity import ShowcaseProjectEntity
from backend.models.user import User
from backend.services.exceptions import ResourceNotFoundException
from backend.services.permission import PermissionService

from ..models.showcase import ShowcaseProject


class ShowcaseService:
    def __init__(
        self,
        session: Session = Depends(db_session),
        permission: PermissionService = Depends(),
    ):
        self._session = session
        self._permission = permission

    # Get all showcases
    def get_showcases(self) -> list[ShowcaseProject]:
        query = select(ShowcaseProjectEntity)
        showcase_entities = self._session.scalars(query).all()

        return [entity.to_model() for entity in showcase_entities]

    # Get showcase by id
    def get_showcase(self, id: int) -> ShowcaseProject:
        showcase_entity = self._session.get(ShowcaseProjectEntity, id)

        if showcase_entity is None:
            raise ResourceNotFoundException(f"No showcase found with matching ID: {id}")

        return showcase_entity.to_model()

    # Create new showcase
    def create_showcase(
        self, subject: User, showcase: ShowcaseProject
    ) -> ShowcaseProject:

        # Checks if the showcase already exists in the table
        if showcase.id:
            # Set id to None so database can handle setting the id
            showcase.id = None

        showcase_entity = ShowcaseProjectEntity.from_model(subject, showcase)

        self._session.add(showcase_entity)
        self._session.commit()

        return showcase_entity.to_model()

    # Update existing showcase
    def modify_showcase(
        self, subject: User, showcase: ShowcaseProject
    ) -> ShowcaseProject:
        showcase_entity = self._session.get(ShowcaseProjectEntity, showcase.id)

        # Showcase attempting to be updated does not exist
        if showcase_entity is None:
            raise ResourceNotFoundException(
                f"No showcase found with matching ID: {showcase.id}"
            )

        # Check to see if user is administrator if they are not the author
        if showcase_entity.author_profile.pid != subject.pid:
            self._permission.enforce(
                subject, "showcase.modify_showcase", f"showcase/{showcase_entity.id}"
            )

        showcase_entity.title = showcase.title
        showcase_entity.shorthand = showcase.shorthand
        showcase_entity.thumbnail = showcase.thumbnail
        showcase_entity.short_description = showcase.short_description
        showcase_entity.text_body = showcase.text_body
        showcase_entity.author = showcase.author
        showcase_entity.onyen = showcase.onyen
        showcase_entity.public = showcase.public

        self._session.commit()

        return showcase_entity.to_model()

    # Delete existing showcase
    def remove_showcase(self, subject: User, id: int) -> ShowcaseProject:
        showcase_entity = self._session.get(ShowcaseProjectEntity, id)

        # Showcase attempting to be deleted does not exist
        if showcase_entity is None:
            raise ResourceNotFoundException(f"No showcase found with matching id: {id}")

        # Check to see if user is administrator if they are not the author
        if showcase_entity.author_profile.pid != subject.pid:
            self._permission.enforce(
                subject, "showcase.remove_showcase", f"showcase/{id}"
            )

        self._session.delete(showcase_entity)
        self._session.commit()

        return showcase_entity.to_model()
