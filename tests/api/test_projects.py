import json
from datetime import datetime, timezone
from unittest.mock import Mock
import uuid

from zabunifund.api import crud
from zabunifund.database.models import Project


def test_post_project(test_app, monkeypatch):
    test_request_payload = {
        "title": "something",
        "ptype": "Purchase Order",
        "customer": "bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        "description": "Supply of Sanitizers",
        "po_number": "PO-KEMSA-001",
        "po_issue_date": "2023-11-14",
        "po_delivery_date": "2023-11-14",
        "po_value": 1000000,
        "po_currency": "Kenyan Shilling",
    }

    test_db_project = Project(
        uid="f01a2119-7f25-4a27-82df-28dc2afc0583",
        title="something",
        ptype="Purchase Order",
        customer=uuid.UUID("bb9b3135-9443-4d06-b946-cb4f0672a1f3"),
        description="Supply of Sanitizers",
        po_number="PO-KEMSA-001",
        po_issue_date="2023-11-14",
        po_delivery_date="2023-11-14",
        po_value=1000000,
        po_currency="Kenyan Shilling",
        created="2023-11-09T11:59:01",
        updated="2023-11-09T11:59:01",
    )

    async def mock_create(payload):
        return test_db_project

    monkeypatch.setattr(crud, "create", mock_create)

    response = test_app.post(
        "/projects/",
        content=json.dumps(test_request_payload),
    )

    assert response.status_code == 201
    assert response.json() == test_db_project.dict()


def test_post_project_invalid_json(test_app):
    response = test_app.post("/projects/", content=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_app.post(
        "/projects/", content=json.dumps({"title": "1", "description": "2"})
    )
    assert response.status_code == 422


def test_post_project_invalid_type(test_app):
    test_request_payload = {
        "title": "Supply of meds",
        "ptype": "Other",
        "customer": "bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        "description": "Supply of Sanitizers",
        "po_number": "PO-KEMSA-001",
        "po_issue_date": "2023-11-14",
        "po_delivery_date": "2023-11-14",
        "po_value": 1000000,
        "po_currency": "Kenyan Shilling",
    }

    response = test_app.post("/projects/", content=json.dumps(test_request_payload))
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "value is not a valid enumeration member; permitted: 'Purchase Order'"
    )


def test_get_project(test_app, monkeypatch):
    test_db_project = Project(
        uid="f01a2119-7f25-4a27-82df-28dc2afc0583",
        title="something",
        ptype="Purchase Order",
        customer="bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        description="Supply of Sanitizers",
        po_number="PO-KEMSA-001",
        po_issue_date="2023-11-14",
        po_delivery_date="2023-11-14",
        po_value=1000000,
        po_currency="Kenyan Shilling",
        created="2023-11-09T11:59:01",
        updated="2023-11-09T11:59:01",
    )

    async def mock_read(uid):
        return test_db_project

    monkeypatch.setattr(crud, "read", mock_read)

    response = test_app.get("/projects/92e00754-15d9-4572-8d07-81e9344b76a6")
    assert response.status_code == 200
    assert response.json() == test_db_project.dict()


def test_get_project_incorrect_id(test_app, monkeypatch):
    async def mock_read(uid):
        return None

    monkeypatch.setattr(crud, "read", mock_read)

    response = test_app.get("/projects/92e00754-15d9-4572-8d07-81e9344b76a6")
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_read_all_projects(test_app, monkeypatch):
    test_db_projects = [
        Project(
            uid="92e00754-15d9-4572-8d07-81e9344b76a6",
            title="something",
            ptype="Purchase Order",
            customer="bb9b3135-9443-4d06-b946-cb4f0672a1f3",
            description="Supply of Sanitizers",
            po_number="PO-KEMSA-001",
            po_issue_date="2023-11-14",
            po_delivery_date="2023-11-14",
            po_value=1000000,
            po_currency="Kenyan Shilling",
            created="2023-11-09T11:59:01",
            updated="2023-11-09T11:59:01",
        ),
        Project(
            uid="f01a2119-7f25-4a27-82df-28dc2afc0583",
            title="something",
            ptype="Purchase Order",
            customer="bb9b3135-9443-4d06-b946-cb4f0672a1f3",
            description="Supply of Sanitizers",
            po_number="PO-KEMSA-002",
            po_issue_date="2023-11-14",
            po_delivery_date="2023-11-14",
            po_value=1000000,
            po_currency="Kenyan Shilling",
            created="2023-11-09T11:59:01",
            updated="2023-11-09T11:59:01",
        ),
    ]

    async def mock_read_all():
        return test_db_projects

    monkeypatch.setattr(crud, "read_all", mock_read_all)

    response = test_app.get("/projects/")
    assert response.status_code == 200
    assert response.json() == [p.dict() for p in test_db_projects]


def test_update_project(test_app, monkeypatch):
    test_update_data = {
        "title": "something",
        "ptype": "Purchase Order",
        "customer": "bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        "description": "Supply of Sanitizers",
        "po_number": "PO-KEMSA-001",
        "po_issue_date": "2023-11-14",
        "po_delivery_date": "2023-11-14",
        "po_value": 1000000,
        "po_currency": "Kenyan Shilling",
    }

    test_db_project = Project(
        uid="f01a2119-7f25-4a27-82df-28dc2afc0583",
        title="something",
        ptype="Purchase Order",
        customer="bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        description="Supply of Sanitizers",
        po_number="PO-KEMSA-001",
        po_issue_date="2023-11-14",
        po_delivery_date="2023-11-14",
        po_value=1000000,
        po_currency="Kenyan Shilling",
        created="2023-11-09T11:59:01",
        updated="2023-11-09T11:59:01",
    )

    async def mock_update(uid, payload):
        return test_db_project

    monkeypatch.setattr(crud, "update", mock_update)

    response = test_app.put(
        "/projects/f01a2119-7f25-4a27-82df-28dc2afc0583/",
        content=json.dumps(test_update_data),
    )
    assert response.status_code == 200
    assert response.json() == test_db_project.dict()


def test_update_project_invalid(test_app, monkeypatch):
    test_update_data = {
        "title": "something",
        "ptype": "Purchase Order",
        "customer": "bb9b3135-9443-4d06-b946-cb4f0672a1f3",
        "description": "Supply of Sanitizers",
        "po_number": "PO-KEMSA-001",
        "po_issue_date": "2023-11-14",
        "po_delivery_date": "2023-11-14",
        "po_value": 1000000,
        "po_currency": "Kenyan Shilling",
    }

    async def mock_update(uid, payload):
        return None

    monkeypatch.setattr(crud, "update", mock_update)

    response = test_app.put(
        f"/projects/f01a2119-7f25-4a27-82df-28dc2afc0583/",
        content=json.dumps(test_update_data),
    )
    assert response.status_code == 404


def test_remove_project(test_app, monkeypatch):
    async def mock_delete(uid):
        return 1

    monkeypatch.setattr(crud, "delete", mock_delete)
    response = test_app.delete("/projects/f01a2119-7f25-4a27-82df-28dc2afc0583/")
    assert response.status_code == 200


def test_remove_project_incorrect_id(test_app, monkeypatch):
    response = test_app.delete("/projects/1/")
    assert response.status_code == 422

    async def mock_delete(uid):
        return 0

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/projects/f01a2119-7f25-4a27-82df-28dc2afc0583/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"
