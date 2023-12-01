import reflex as rx
from zabunifund import styles

from zabunifund.components.navbar import navbar
from zabunifund.components.sidedrawer import sidedrawer
from zabunifund.components.inner_display import projects_display
from zabunifund.components.modal import add_project_modal


def home() -> rx.Component:
    """The user home page"""
    return rx.vstack(
        navbar(),
        sidedrawer(),
        add_project_modal(),
        projects_display(),
        style=styles.page_style,
    )
