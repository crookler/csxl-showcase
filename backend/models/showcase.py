from pydantic import BaseModel


class ShowcaseProject(BaseModel):
    id: int | None
    name: str
    thumbnail: str
    short_description: str
    long_description: str
    website: str
    email: str
    author: str
    linked_in: str
    heel_life: str
    public: bool
    slug: str
    shorthand: str
