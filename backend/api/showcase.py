from fastapi import APIRouter, Depends

from backend.api.authentication import registered_user
from backend.models.user import User

from ..models.showcase import ShowcaseProject
from ..services.showcase import ShowcaseService

api = APIRouter(prefix="/api/showcase")
openapi_tags = {
    "name": "Showcases",
    "description": "Create, retrieve, update, and delete showcase posts.",
}


# GET /api/showcase
@api.get("", response_model=list[ShowcaseProject], tags=["Showcase"])
def get_showcases(
    showcase_service: ShowcaseService = Depends(),
) -> list[ShowcaseProject]:
    return showcase_service.get_showcases()


# GET /api/showcase/{slug}
@api.get("/{id}", response_model=ShowcaseProject, tags=["Showcase"])
def get_showcase(
    id: int,
    showcase_service: ShowcaseService = Depends(),
) -> list[ShowcaseProject]:
    return showcase_service.get_showcase(id)


# POST /api/showcase
@api.post("", response_model=ShowcaseProject, tags=["Showcase"])
def new_showcase(
    showcase: ShowcaseProject,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.create_showcase(subject, showcase)


# PUT /api/showcase
@api.put("", response_model=ShowcaseProject, tags=["Showcase"])
def update_showcase(
    showcase: ShowcaseProject,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.modify_showcase(subject, showcase)


# DELETE /api/showcase/{slug}
@api.delete("/{id}", response_model=ShowcaseProject, tags=["Showcase"])
def delete_showcase(
    id: int,
    subject: User = Depends(registered_user),
    showcase_service: ShowcaseService = Depends(),
) -> ShowcaseProject:
    return showcase_service.remove_showcase(subject, id)
