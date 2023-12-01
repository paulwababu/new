import reflex as rx

from zabunifund import styles
from zabunifund.components.inner_display import project_display
from zabunifund.components.modal import update_status_modal
from zabunifund.components.navbar import navbar_base
from zabunifund.components.sidedrawer import sidedrawer


def project() -> rx.Component:
    """The project page"""
    return rx.vstack(
        navbar_base(),
        sidedrawer(),
        update_status_modal(),
        project_display(),
        style=styles.page_style,
    )
