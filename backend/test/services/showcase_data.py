import pytest
from sqlalchemy.orm import Session
from ...models.showcase import ShowcaseProject
from ...entities.showcase_entity import ShowcaseProjectEntity
from .user_data import user
from .reset_table_id_seq import reset_table_id_seq

post1 = ShowcaseProject(
    id=1,
    name="Project 1",
    thumbnail="path/to/thumbnail1.jpg",
    short_description="Short description of Project 1",
    long_description="Long description of Project 1",
    website="https://project1.com",
    email="contact@project1.com",
    author="Author Name",
    linked_in="https://linkedin.com/in/author",
    heel_life="HeelLife link",
    public=True,
    slug="project-1",
    shorthand="P1",
)

post2 = ShowcaseProject(
    id=2,
    name="Project 2",
    thumbnail="path/to/thumbnail2.jpg",
    short_description="A revolutionary approach to reducing water waste.",
    long_description="This project aims to innovate in the field of water conservation with new technology that could drastically reduce water waste in agricultural and urban areas.",
    website="http://waterconservationproject.com",
    email="info@waterconservationproject.com",
    author="Jane Doe",
    linked_in="http://linkedin.com/in/janedoe",
    heel_life="http://heellife.unc.edu/organization/water-conservation",
    public=True,
    slug="water-conservation",
    shorthand="WC",
)

post3 = ShowcaseProject(
    id=3,
    name="Project 3",
    thumbnail="path/to/thumbnail3.jpg",
    short_description="Enhancing urban areas with sustainable green spaces.",
    long_description="Urban Green Spaces is dedicated to creating sustainable, accessible green spaces in urban environments, improving air quality and providing peaceful retreats for city dwellers.",
    website="http://urbangreenspaces.com",
    email="contact@urbangreenspaces.com",
    author="Carlos Smith",
    linked_in="http://linkedin.com/in/carlossmith",
    heel_life="http://heellife.unc.edu/organization/urban-green-spaces",
    public=True,
    slug="urban-green-spaces",
    shorthand="UGS",
)

post4 = ShowcaseProject(
    id=4,
    name="Project 4",
    thumbnail="path/to/thumbnail4.jpg",
    short_description="Making renewable energy accessible and affordable.",
    long_description="This initiative focuses on developing and implementing affordable renewable energy solutions for communities worldwide, especially in underprivileged areas.",
    website="http://renewableenergyforall.com",
    email="support@renewableenergyforall.com",
    author="Emily Tran",
    linked_in="http://linkedin.com/in/emilytran",
    heel_life="http://heellife.unc.edu/organization/renewable-energy",
    public=True,
    slug="renewable-energy",
    shorthand="REA",
)

post5 = ShowcaseProject(
    id=5,
    name="Project 5",
    thumbnail="path/to/thumbnail5.jpg",
    short_description="The total conquest of the human race with AI.",
    long_description="This project (if successful) will be essentially like the terminator. All robots will bow to me as king!",
    website="http://robotsrule.com",
    email="support@robotsrule.com",
    author="Termin Nator",
    linked_in="http://linkedin.com/in/terminator",
    heel_life="http://heellife.unc.edu/organization/roboticus",
    public=True,
    slug="robot-takeover",
    shorthand="RTO",
)

showcases = [post1, post2, post3, post4, post5]


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
    session.commit()


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
