from datetime import datetime, timezone
import uuid

import reflex as rx

from zabunifund.api.schemas import ProjectSchema
from zabunifund.database.models import Project


async def create(payload: ProjectSchema):
    with rx.session() as session:
        session.expire_on_commit = False
        project_db = Project(
            title=payload.title,
            customer=payload.customer,
            description=payload.description,
            ptype=payload.ptype,
            po_number=payload.po_number,
            po_issue_date=payload.po_issue_date,
            po_delivery_date=payload.po_delivery_date,
            po_value=payload.po_value,
            po_currency=payload.po_currency,
        )

        session.add(project_db)
        session.commit()
    return project_db


async def read(uid: uuid.UUID):
    with rx.session() as session:
        project = session.exec(Project.select.where(Project.uid == uid)).first()
    return project


async def read_all():
    with rx.session() as session:
        projects = session.query(Project).order_by(Project.created).all()
    return projects


async def update(uid: uuid.UUID, payload: ProjectSchema):
    with rx.session() as session:
        session.expire_on_commit = False
        project_db = session.exec(Project.select.where(Project.uid == uid)).first()
        if not project_db:
            return None
        for k, v in payload.items():
            setattr(project_db, k, v)
            project_db.updated = datetime.now(timezone.utc)
        session.add(project_db)
        session.commit()
    return project_db


async def delete(uid: uuid.UUID):
    with rx.session() as session:
        project_db = session.exec(Project.select.where(Project.uid == uid)).first()
        if not project_db:
            return 0
        session.delete(project_db)
        session.commit()
    return 1
