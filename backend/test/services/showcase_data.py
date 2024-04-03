import pytest
from sqlalchemy.orm import Session
from ...models.showcase import ShowcaseProject
from ...entities.showcase_entity import ShowcaseProjectEntity
from .user_data import user
from .reset_table_id_seq import reset_table_id_seq

post1 = ShowcaseProject(
    id=1,
    name="The Best Thing I Have Ever Made",
    thumbnail="Thumbnail",
    short_description="Short",
    long_description="Long",
    website="Website",
    email="Email",
    author=user,
    linked_in="LinkedIn",
    heel_life="Heel Life",
    public=True,
    slug="best",
    shorthand="bst",
)

post2 = ShowcaseProject(
    id=2,
    name="The Worst Thing I Have Ever Made",
    thumbnail="Thumbnail",
    short_description="Short",
    long_description="Long",
    website="Website",
    email="Email",
    author=user,
    linked_in="LinkedIn",
    heel_life="Heel Life",
    public=True,
    slug="worst",
    shorthand="wst",
)

post3 = ShowcaseProject(
    id=3,
    name="The Most Mid Thing I Have Ever Made",
    thumbnail="Thumbnail",
    short_description="Short",
    long_description="Long",
    website="Website",
    email="Email",
    author=user,
    linked_in="LinkedIn",
    heel_life="Heel Life",
    public=True,
    slug="middle",
    shorthand="mid",
)

showcases = [post1, post2, post3]


def insert_fake_data(session: Session):
    global showcases
    entities = []
    for showcase in showcases:
        entity = ShowcaseProjectEntity.from_model(showcase)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(
        session, ShowcaseProjectEntity, ShowcaseProjectEntity.id, len(showcases) + 1
    )
    session.commit()  # Commit to ensure User IDs in database


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
