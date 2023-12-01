import reflex as rx

from zabunifund import styles
from zabunifund.components.modal import add_customer_modal

from zabunifund.components.navbar import navbar
from zabunifund.components.sidedrawer import sidedrawer


def customers() -> rx.Component:
    """The customers page"""
    return rx.vstack(
        navbar(),
        sidedrawer(),
        add_customer_modal(),
        style=styles.page_style,
    )
