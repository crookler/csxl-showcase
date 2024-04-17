from pydantic import BaseModel


class ShowcaseProject(BaseModel):
    id: int | None = None
    title: str
    shorthand: str
    thumbnail: str
    short_description: str
    text_body: str
    author: str
    onyen: str
    public: bool
