from sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self

from backend.entities.user_entity import UserEntity
from backend.models.showcase import ShowcaseProject
from .entity_base import EntityBase


class ShowcaseProjectEntity(EntityBase):
    __tablename__ = "showcase"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, default="")
    thumbnail: Mapped[str] = mapped_column(String)
    short_description: Mapped[str] = mapped_column(String)
    long_description: Mapped[str] = mapped_column(String)
    website: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    author_pid: Mapped[int] = mapped_column(ForeignKey("user.pid"))
    linked_in: Mapped[str] = mapped_column(String)
    heel_life: Mapped[str] = mapped_column(String)
    public: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    shorthand: Mapped[str] = mapped_column(String)

    # Establish one-to-many relationship for authors and projects (one author can have many projects)
    author: Mapped["UserEntity"] = relationship(back_populates="showcases")

    @classmethod
    def from_model(cls, model: ShowcaseProject) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            thumbnail=model.thumbnail,
            short_description=model.short_description,
            long_description=model.long_description,
            website=model.website,
            email=model.email,
            author_pid=model.author.pid,
            linked_in=model.linked_in,
            heel_life=model.heel_life,
            public=model.public,
            slug=model.slug,
            shorthand=model.shorthand,
        )

    def to_model(self) -> ShowcaseProject:
        return ShowcaseProject(
            id=self.id,
            name=self.name,
            thumbnail=self.thumbnail,
            short_description=self.short_description,
            long_description=self.long_description,
            website=self.website,
            email=self.email,
            author=self.author.to_model(),
            linked_in=self.linked_in,
            heel_life=self.heel_life,
            public=self.public,
            slug=self.slug,
            shorthand=self.shorthand,
        )
