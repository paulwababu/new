"""Welcome to Zabuni fund! This file outlines the steps to create a basic app."""

import reflex as rx

from zabunifund import styles
from zabunifund.api.projects import project_router
from zabunifund.pages.customers import customers
from zabunifund.pages.home import home
from zabunifund.pages.index import index
from zabunifund.pages.project import project
from zabunifund.state import HomeState, ProjectState, State

# Add state and page to the app.
app = rx.App(state=State, style=styles.base_style)
app.add_page(index, on_load=[State.set_current_item()])
app.add_page(
    home,
    route="/projects",
    on_load=[HomeState.load_projects(), HomeState.set_current_item("projects")],
)
app.add_page(customers, route="/customers")
app.add_page(
    project,
    route="/projects/[uid]",
    on_load=[State.set_current_item("project"), ProjectState.load_project()],
)
app.api.include_router(project_router)
app.compile()
