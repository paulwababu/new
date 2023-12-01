"""API methods to handle projects."""
import json
from typing import List
import uuid

from fastapi import APIRouter, Request, status, Path
from fastapi.exceptions import HTTPException

from zabunifund.api.schemas import ProjectSchema

from zabunifund.database.models import Project

from zabunifund.api import crud


async def get_projects():
    """Get a list of all the projects."""
    return await crud.read_all()


async def get_project(uid: uuid.UUID):
    """Get the project associated with uid."""
    project = await crud.read(uid)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return project


async def post_project(payload: ProjectSchema):
    """Add a new project."""
    return await crud.create(payload)


async def put_project(payload: ProjectSchema, uid: uuid.UUID):
    """Update the project associated with uid."""
    updated_project = await crud.update(uid, payload)

    if not updated_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return updated_project


async def delete_project(uid: uuid.UUID):
    """Delete the project associated with uid."""
    deleted_count = await crud.delete(uid)
    if not deleted_count:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return deleted_count


project_router = APIRouter(prefix="/projects", tags=["projects"])

project_router.add_api_route(
    "",
    post_project,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
    response_model=Project,
)
project_router.add_api_route(
    "", get_projects, methods=["GET"], response_model=List[Project]
)
project_router.add_api_route(
    "/{uid}", get_project, methods=["GET"], response_model=Project
)
project_router.add_api_route(
    "/{uid}", put_project, methods=["PUT"], response_model=Project
)
project_router.add_api_route(
    "/{uid}",
    delete_project,
    methods=["DELETE"],
    response_model=int,
    status_code=status.HTTP_200_OK,
)
