from fastapi import APIRouter, Depends

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
