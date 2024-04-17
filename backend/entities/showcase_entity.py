from sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self

from backend.entities.user_entity import UserEntity
from backend.models.showcase import ShowcaseProject
from backend.models.user import User
from .entity_base import EntityBase


class ShowcaseProjectEntity(EntityBase):
    __tablename__ = "showcase"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False, default="")
    shorthand: Mapped[str] = mapped_column(String)
    thumbnail: Mapped[str] = mapped_column(String)
    short_description: Mapped[str] = mapped_column(String)
    text_body: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    onyen: Mapped[str] = mapped_column(String, nullable=False)
    public: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    # Establish one-to-many relationship between a given user and their showcases
    author_profile: Mapped["UserEntity"] = relationship(back_populates="showcases")

    @classmethod
    def from_model(cls, subject: User, model: ShowcaseProject) -> Self:
        return cls(
            id=model.id,
            title=model.title,
            shorthand=model.shorthand,
            thumbnail=model.thumbnail,
            short_description=model.short_description,
            text_body=model.text_body,
            author=model.author,
            onyen=model.onyen,
            public=model.public,
            author_id=subject.id,
        )

    def to_model(self) -> ShowcaseProject:
        return ShowcaseProject(
            id=self.id,
            title=self.title,
            shorthand=self.shorthand,
            thumbnail=self.thumbnail,
            short_description=self.short_description,
            text_body=self.text_body,
            author=self.author,
            onyen=self.onyen,
            public=self.public,
        )
