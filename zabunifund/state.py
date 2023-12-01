import asyncio
import json
from typing import List

import httpx
import reflex as rx

from enum import Enum

import logging


logger = logging.getLogger()


class State(rx.State):
    """The app state."""

    # The current item.
    current_item = ""

    def set_current_item(self, item: str = ""):
        self.current_item = item

    user = 0


class IndexState(State):
    async def handle_login(self):
        self.user = 1
        return rx.redirect("/projects")

    def handle_home(self):
        if self.user:
            return rx.redirect("/projects")
        else:
            return rx.redirect("/")

    def handle_logout(self):
        self.user = 0
        return rx.redirect("/")


class ProjectTypesEnum(str, Enum):
    purchase_order = "Purchase Order"


class HomeState(IndexState):
    # Whether the drawer is open.
    drawer_open: bool = False

    # Whether the modal is open.
    modal_open: bool = False

    # Sidedrawer menu items
    sidedrawer_menu_items = ["Projects", "Customers", "Suppliers"]

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open

    def handle_sidedrawer_item(self, item: str):
        """Set the name of the current item selected.

        Args:
            item: The name of the item selected.
        """
        self.current_item = item
        self.toggle_drawer()

        match self.current_item:
            case "Projects":
                return rx.redirect("/projects")

            case "Customers":
                return rx.redirect("/customers")
            # case "Suppliers":
            # return rx.redirect("/suppliers")

    project_types: List[str] = [p.value for p in ProjectTypesEnum]

    project_statuses: List[str] = ["DRAFT", "SUBMITTED", "CLOSED"]
    project_status_commands: List[str] = ["Submit", "Close"]

    # TODO: Load from db/api
    list_of_customers: List[str] = [
        {"uid": "bb9b3135-9443-4d06-b946-cb4f0672a1f3", "name": "KEMSA"}
    ]

    list_of_customer_names = [c["name"] for c in list_of_customers]

    # TODO: Load from db/api
    currencies: List[str] = ["US Dollar", "Kenyan Shilling"]

    base_url = f"http://localhost:8000"
    projects_url = f"{base_url}/projects"
    customers_url = f"{base_url}/customers"
    suppliers_url = f"{base_url}/suppliers"

    projects: List[dict] = []

    selected_project: dict = {}

    projects_draft_count = 0
    projects_submitted_count = 0
    projects_closed_count = 0

    # Projects
    async def load_projects(self):
        headers = {"Content-Type": "application/json"}
        async with httpx.AsyncClient() as client:
            res = await client.get(
                self.projects_url,
                headers=headers,
            )

        response_code = res.status_code
        if response_code == 200:
            loaded_projects = res.json()[::-1]
            # augment the returned list with extra data
            for p in loaded_projects:
                p["customer_name"] = self.customer_uid_to_name(p["customer"])
            self.projects = loaded_projects
            self.projects_draft_count = len(
                [p for p in self.projects if p["status"] == "DRAFT"]
            )
            self.projects_submitted_count = len(
                [p for p in self.projects if p["status"] == "SUBMITTED"]
            )

            self.projects_closed_count = len(
                [p for p in self.projects if p["status"] == "CLOSED"]
            )

    async def handle_project_submit(self, project_form_data: dict):
        """Handle project form submit."""

        # Resolve customer
        customer_name = project_form_data["customer"]
        project_form_data["customer"] = self.customer_name_to_uid(customer_name)

        data = json.dumps(project_form_data)
        headers = {"Content-Type": "application/json"}

        """Create project through the api"""
        async with httpx.AsyncClient() as client:
            res = await client.post(
                self.projects_url,
                data=data,
                headers=headers,
            )

        response_code = res.status_code
        if response_code == 200 | 201:
            response = res.json()
            self.toggle_modal()
            await self.load_projects()

            response["customer_name"] = self.customer_uid_to_name(response["customer"])
            self.selected_project = response
            return rx.redirect(f"/projects/{self.selected_project['uid']}")

        else:
            response = res.content.decode()
            logger.error(response)

    def customer_uid_to_name(self, uid: str):
        customer_name = [c["name"] for c in self.list_of_customers if c["uid"] == uid][
            0
        ]

        return customer_name

    def customer_name_to_uid(self, name: str):
        customer_uid = [c["uid"] for c in self.list_of_customers if c["name"] == name][
            0
        ]

        return customer_uid

    def set_selected_project(self, project: dict):
        self.selected_project = project
        self.set_current_item("Project")
        return rx.redirect(f"/projects/{project['uid']}")


class ProjectState(HomeState):
    async def load_project(self):
        if not self.selected_project:
            headers = {"Content-Type": "application/json"}
            current_page_raw_path = self.router.page.raw_path.rstrip(
                self.router.page.raw_path[-1]
            )

            async with httpx.AsyncClient() as client:
                res = await client.get(
                    f"{self.base_url}{current_page_raw_path}",
                    headers=headers,
                )

            response_code = res.status_code
            if response_code == 200:
                response = res.json()
                response["customer_name"] = self.customer_uid_to_name(
                    response["customer"]
                )
                self.selected_project = response


class CustomersState(HomeState):
    def handle_customer_submit(self, customer_form_data: dict):
        """Handle customer form submit."""
        pass
