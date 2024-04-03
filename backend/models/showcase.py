from pydantic import BaseModel
from .user import User


class ShowcaseProject(BaseModel):
    id: int | None
    name: str
    thumbnail: str
    short_description: str
    long_description: str
    website: str
    email: str
    author: User
    linked_in: str
    heel_life: str
    public: bool
    slug: str
    shorthand: str
