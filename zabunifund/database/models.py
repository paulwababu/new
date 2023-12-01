"""Models used by the app."""
from datetime import date, datetime, timezone
import uuid

from sqlmodel import Column, DateTime, Field, func
from sqlalchemy.dialects import postgresql as psql

import reflex as rx


class Project(rx.Model, table=True):
    """Project model."""

    uid: uuid.UUID = Field(
        sa_column=Column(psql.UUID(as_uuid=True)), default=uuid.uuid4(), unique=True
    )
    title: str
    ptype: str
    customer: uuid.UUID = Field(index=True)
    description: str
    po_number: str
    po_issue_date: date
    po_delivery_date: date
    po_value: float
    po_currency: str
    status: str = Field(default="DRAFT")
    created: datetime = Field(
        default=datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
        nullable=False,
    )
    updated: datetime = Field(
        default=datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
        nullable=False,
    )

    def dict(self, *args, **kwargs) -> dict:
        """Serialize method."""
        d = super().dict(*args, **kwargs)
        d["created"] = self.created.replace(microsecond=0).isoformat()
        d["updated"] = self.updated.replace(microsecond=0).isoformat()
        d["po_issue_date"] = self.po_issue_date.isoformat()
        d["po_delivery_date"] = self.po_delivery_date.isoformat()
        d["uid"] = str(self.uid)
        d["customer"] = str(self.customer)
        # exlude some fields from being exposed
        del d["id"]
        return d
