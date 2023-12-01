import uuid
from datetime import date, datetime

import reflex as rx
from pydantic import BaseModel, Field, ValidationError, validator

from zabunifund.state import HomeState, ProjectTypesEnum


class ProjectSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    ptype: ProjectTypesEnum
    customer: uuid.UUID
    description: str = Field(..., min_length=3, max_length=250)
    po_number: str = Field(..., min_length=3, max_length=100)
    po_issue_date: date
    po_delivery_date: date
    po_value: float
    po_currency: str
