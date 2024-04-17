# Student Project Technical Specification Documentation

**Team B5 Members:** [Ethan Crook](https://github.com/crookler), [Noah Weaver](https://github.com/noahweaves), [Avi Kumar](https://github.com/aviomg)

## Overview

Describes many technical details about our codebase, explains certain design decisions, and recommends procedure for new developers.

## Data and the API

**Project Model**

The backend showcase model can be found at /workspace/backend/models/showcase.py.

Here is the current state of our ShowcaseProject model which contains all the data relavent to a specific project on the showcase page:

```python
class ShowcaseProject(BaseModel):
    id: int | None
    title: str
    shorthand: str
    thumbnail: str
    short_description: str
    text_body: str
    author: str
    onyen: str
    public: bool
```

Currently, we're storing every field as a primitive datatype. Only some of these fields are consquestial as of now, specifically thumbnail, though we will make us of it shortly.

Here is an example of a showcase projects literal representation:
```python
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
```


**API Routes**

We have several API routes which expose and manipulate showcase data from the database. They can be found at /workspace/backend/api/showcase.py.

<u>GET:</u>

This route is used to display all the projects on the showcase page.
```python
@api.get("", response_model=list[ShowcaseProject], tags=["Showcase"])
def get_showcases(
    showcase_service: ShowcaseService = Depends(),
) -> list[ShowcaseProject]:
    return showcase_service.get_showcases()
```
<u>GET (by ID):</u>

This route is used to retrieve a single showcase project from the database. This will be used to view a single project's data on the project page. 
```python
@api.get("/{id}", response_model=ShowcaseProject, tags=["Showcase"])
def get_showcase(
    id: int,
    showcase_service: ShowcaseService = Depends(),
) -> list[ShowcaseProject]:
    return showcase_service.get_showcase(id)
```
<u>PUT:</u> 

This route is used when users want to edit projects using our showcase editor form.
```python
@api.post("", response_model=ShowcaseProject, tags=["Showcase"])
def new_showcase(
    showcase: ShowcaseProject,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.create_showcase(subject, showcase)
```
<u>POST:</u>

This route is used when users want to create new projects through the showcase page.
```python
@api.put("", response_model=ShowcaseProject, tags=["Showcase"])
def update_showcase(
    showcase: ShowcaseProject,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.modify_showcase(subject, showcase)
```
<u>DELETE:</u> 

This route is useed when a project is deleted from the showcase page. 
```python
@api.delete("/{id}", response_model=ShowcaseProject, tags=["Showcase"])
def delete_showcase(
    id: int,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.remove_showcase(subject, id)
```


## Database and Entities: 

While our database entity fields are directly related to the showcase model's fields, there are a number of integrity contraints to garentee proper behavior: 

```python
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
```
^ found at /workspace/backend/entities/showcase_entity.py

We chose to use the ID integer field as the primary key and added the autoincrement perameter for ease of use.

For fields that are integral to the functionality of the feature, we added the 'nullable=false' perameter to ensure that we can use them to display info, authenticate users, and manipulate data. 


## Design choices:

**Showcase Page Widgets**

A major design desicion was what size to make the individual project displays on the project page. Smaller individual widgets would allow for a user to see more projects at as well as limit the information we have to display in each widget. Larger widgets could make for a more interesting user experience and leave room for more creative design. 

We decided to include larger widgets which include thumbnail images for each project to draw in users and make each project more distinct on the page.

**Entity/Model and the slug**

Initially, we had a slug field in each showcase project based of the title of the project. This presented some issues because we did not want to restrict titles to be unique. This meant that if a two titles were the same, either users would need to adjust the slug manually, or we would need to implement some automatic slug manipulation. 

In order to streamline the process, we decided to eliminate the slug field altogether and use ID as our tool for routing URLs and manipulating the database.

## Understanding our features:

For new developers the first thing to keep in mind is that this is a full stack feature with a robust frontend and backend. It may be benificial to start dovelopment in a more familiar aspect of the feature (HTML/CSS, frontend service, api methods, etc) but it is important that eventually, you have some familiarity with the full stack. 


**Frontend**

The frontend is made up of a number of components that interact with one another.


Showcase Page 

This is the central page that you can navigate to on the CSXL sidebar. It's job is to display cirtain information from the projects we have in the backend. Navigation to the subcomponents is done primarily throught htis component.


Product Page

This is the page that is currently accessed through the details button on the showcase page. It isn't currently implemented but it will eventually display information about a given project in greater detail, as well as provide direct interaction with specific types of projects. 



Project Card Widget

These are displayed on the showcase page for each product. They display basic information and a thumbnail which is currently just a picture of a goat for every project.


Showcase Editor

Accessed through the edit and create buttons from the showcase page. This is a form for manipulating the database and creating or editing projects. 



**Backend**

The backend works by chaining data through a number of steps. 

1) Database --Sqlalchemy--> 2)Backend service --API methods--> 3)Frontend service 
--Service methods--> 4)Frontend components 


The entity /workspace/backend/entities/showcase_entity.py along with the backend model /workspace/backend/models/showcase.py define the underlying structure for a showcase project in the database. 

The backend service file /workspace/backend/services/showcase.py establishes the database session and defines methods for backend interaction. 

The /workspace/backend/api/showcase.py file interacts with the backend service to establish the API methods. 

Finally, the frontend service at /workspace/frontend/src/app/showcase/showcase.service.ts uses http calls to make data accessible to the frontend components. 


Hopefully this gives you a good overview of our feature. Start familiarizing yourself with these files and before long you'll be an angular master!







