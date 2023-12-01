import reflex as rx

from zabunifund import styles
from zabunifund.components.inner_display import projects_display
from zabunifund.components.modal import add_project_modal
from zabunifund.components.navbar import navbar_no
from zabunifund.components.sidedrawer import sidedrawer
from zabunifund.state import IndexState


def index() -> rx.Component:
    """The index page"""
    return rx.vstack(
        navbar_no(),
        rx.vstack(
            rx.box(
                rx.text(
                    "Zabunifund is a marketplace for funding purchase order projects.",
                    font_weight="bold",
                ),
                rx.text(
                    """            
                Let's say you have a purchase order from a reputable client but your company is facing cashflow issues that might hinder you from servicing the project.
                We will assess the project risk based on the information that you provide us with then we will work with our partners to fund your project so that you're able to service it. 
                Give us a try today.
                """,
                    margin_top="5",
                    margin_bottom="5",
                ),
                rx.button(
                    "Create Account",
                    style=styles.main_button_style,
                    margin_bottom="5",
                ),
                rx.button(
                    "Login",
                    style=styles.main_button_style,
                    margin_bottom="5",
                    on_click=IndexState.handle_login(),
                ),
                px="5",
                py="5",
                border=f"1px solid #E2E3F3",
                border_radius="10px",
                min_h="150px",
            ),
            rx.spacer(),
            width="100%",
            height="100%",
            flex="1",
            max_w="xl",
            align_self="center",
            py="8",
        ),
        style=styles.page_style,
    )
