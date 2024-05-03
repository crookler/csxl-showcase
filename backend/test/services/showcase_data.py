import pytest
from sqlalchemy.orm import Session
from ...models.showcase import ShowcaseProject
from ...entities.showcase_entity import ShowcaseProjectEntity
from .user_data import user
from .reset_table_id_seq import reset_table_id_seq

post1 = ShowcaseProject(
    id=1,
    title="Project 1",
    shorthand="P1",
    thumbnail="path/to/thumbnail1.jpg",
    short_description="Short description of Project 1",
    text_body="Long description of Project 1",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)

wc = ShowcaseProject(
    id=2,
    title="Water Conservation",
    shorthand="WC",
    thumbnail="path/to/thumbnail2.jpg",
    short_description="A revolutionary approach to reducing water waste.",
    text_body="This project aims to innovate in the field of water conservation with new technology that could drastically reduce water waste in agricultural and urban areas.",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)

ugs = ShowcaseProject(
    id=3,
    title="Urban Areas",
    shorthand="UGS",
    thumbnail="path/to/thumbnail3.jpg",
    short_description="Enhancing urban areas with sustainable green spaces.",
    text_body="Urban Green Spaces is dedicated to creating sustainable, accessible green spaces in urban environments, improving air quality and providing peaceful retreats for city dwellers.",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)


showcases = [post1, wc, ugs]

to_add = ShowcaseProject(
    title="Terminator Time",
    shorthand="TT",
    thumbnail="path/to/thumbnail3.jpg",
    short_description="Ruling the world with robots one step at a time.",
    text_body="I want to make it my crystal-clear goal to rule the world with said aforementioned robots.",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)

to_add_conflicting_id = ShowcaseProject(
    id=2,
    title="Terminator Time",
    shorthand="TT",
    thumbnail="path/to/thumbnail3.jpg",
    short_description="Ruling the world with robots one step at a time.",
    text_body="I want to make it my crystal-clear goal to rule the world with said aforementioned robots.",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)

updated_wc = ShowcaseProject(
    id=2,
    title="Water Conservation EDITED",
    shorthand="WC",
    thumbnail="path/to/thumbnail2.jpg",
    short_description="A revolutionary approach to reducing water waste.",
    text_body="This project aims to innovate in the field of water conservation with new technology that could drastically reduce water waste in agricultural and urban areas.",
    author=user.first_name + " " + user.last_name,
    onyen=user.onyen,
    public=True,
)


def insert_fake_data(session: Session):
    global showcases
    entities = []
    for showcase in showcases:
        entity = ShowcaseProjectEntity.from_model(user, showcase)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(
        session, ShowcaseProjectEntity, ShowcaseProjectEntity.id, len(showcases) + 1
    )
    session.commit()


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
