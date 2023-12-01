import reflex as rx

from zabunifund import styles
from zabunifund.state import HomeState, IndexState, State


def hamburger():
    return rx.icon(
        tag="hamburger",
        mr=4,
        on_click=HomeState.toggle_drawer,
        cursor="pointer",
    )


def icon_link():
    return rx.link(
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
        on_click=IndexState.handle_home(),
    )


def breadcrumb():
    return rx.breadcrumb(
        rx.breadcrumb_item(
            rx.link(
                rx.heading("Zabunifund", size="sm"), on_click=IndexState.handle_home()
            )
        ),
        rx.breadcrumb_item(
            rx.text(IndexState.current_item, size="sm", font_weight="normal"),
        ),
    )


def avatar_menu():
    return rx.menu(
        rx.menu_button(
            rx.avatar(size="sm"),
            rx.box(),
        ),
        rx.menu_list(
            rx.menu_item("Profile"),
            rx.menu_divider(),
            rx.menu_item("Settings"),
            rx.menu_divider(),
            rx.menu_item("Logout", on_click=IndexState.handle_logout()),
        ),
    )


def navbar_no():
    return rx.box(
        rx.hstack(
            rx.hstack(
                icon_link(),
                breadcrumb(),
            ),
            justify="space-between",
        ),
        style=styles.navbar_style,
    )


def navbar_base():
    return rx.box(
        rx.hstack(
            rx.hstack(
                hamburger(),
                icon_link(),
                breadcrumb(),
            ),
            rx.hstack(
                avatar_menu(),
                spacing="8",
            ),
            justify="space-between",
        ),
        style=styles.navbar_style,
    )


def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                hamburger(),
                icon_link(),
                breadcrumb(),
            ),
            rx.hstack(
                rx.fragment(
                    rx.icon(tag="search2", style=styles.nav_search_style),
                    rx.text(
                        "Search...",
                        style=styles.nav_search_style,
                        font_weight=400,
                    ),
                ),
                rx.spacer(),
                rx.text("/", style=styles.nav_search_style),
                display=["none", "flex", "flex", "flex", "flex"],
                min_width=["15em", "15em", "15em", "20em", "20em"],
                padding_x="1em",
                height="2em",
                border_radius="20px",
                bg="#FAF8FB",
            ),
            rx.hstack(
                rx.button(
                    "+ Add New",
                    style=styles.main_button_style,
                    on_click=HomeState.toggle_modal,
                ),
                avatar_menu(),
                spacing="8",
            ),
            justify="space-between",
        ),
        style=styles.navbar_style,
    )
