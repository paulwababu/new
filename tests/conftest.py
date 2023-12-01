from fastapi import FastAPI
import pytest
from starlette.testclient import TestClient
from zabunifund.api.projects import project_router
from reflex import constants
from reflex.app import ping


backend_app = FastAPI()

backend_app.include_router(project_router)
backend_app.get(str(constants.Endpoint.PING))(ping)


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(backend_app)
    yield client  # testing happens here
