import reflex as rx

from zabunifund import styles
from zabunifund.state import HomeState


def sidedrawer_item(item: str) -> rx.Component:
    """A sidebar menu item.

    Args:
        item: The menu item.
    """
    return rx.hstack(
        rx.box(
            item,
            on_click=lambda: HomeState.handle_sidedrawer_item(item),
            style=styles.sidedrawer_style,
            color=styles.text_color_blue,
            _hover={"bg": styles.accent_greyish, "color": "#fff"},
            flex="1",
        ),
        color=styles.text_color,
        cursor="pointer",
    )


def sidedrawer() -> rx.Component:
    """The sidebar component."""
    return rx.drawer(
        rx.drawer_overlay(
            rx.drawer_content(
                rx.drawer_header(
                    rx.hstack(
                        rx.box(
                            rx.image(
                                src="http://localhost:3000/favicon.ico",
                                width=30,
                                height="auto",
                            ),
                            p="1",
                            border_radius="6",
                            mr="2",
                        ),
                        rx.heading("Zabunifund", size="sm"),
                        rx.icon(
                            tag="close",
                            on_click=HomeState.toggle_drawer,
                            style=styles.icon_style,
                            placement="right",
                        ),
                    )
                ),
                rx.drawer_body(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Zabunifund is a marketplace to ensure success of your purchase order projects.",
                                font_weight="bold",
                            ),
                            rx.text(
                                """
                                Submit your purchase order project today to get funding!
                                """,
                                margin_top="5",
                                margin_bottom="5",
                            ),
                            px="5",
                            py="5",
                            border=f"1px solid #E2E3F3",
                            border_radius="10px",
                            min_h="150px",
                            margin_bottom="50px",
                        ),
                        rx.foreach(
                            HomeState.sidedrawer_menu_items,
                            lambda item: sidedrawer_item(item),
                        ),
                        align_items="stretch",
                    )
                ),
            ),
        ),
        placement="left",
        is_open=HomeState.drawer_open,
    )
