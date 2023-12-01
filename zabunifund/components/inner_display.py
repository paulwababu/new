import reflex as rx
from zabunifund import styles

from zabunifund.state import HomeState, ProjectState


def projects_display():
    return rx.hstack(
        rx.box(
            rx.hstack(
                rx.heading("Top Projects", size="sm"),
            ),
            rx.spacer(min_h="5"),
            rx.hstack(rx.input(placeholder="Search Projects...")),
            style=styles.sidebar_style,
        ),
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.heading("Draft", size="md"),
                    rx.hstack(
                        rx.icon(
                            tag="edit",
                        ),
                        rx.heading(HomeState.projects_draft_count),
                        rx.spacer(),
                    ),
                    style=styles.dashboard_info_box_style,
                ),
                rx.vstack(
                    rx.heading("Submitted", size="md"),
                    rx.hstack(
                        rx.icon(
                            tag="check_circle",
                        ),
                        rx.heading(HomeState.projects_submitted_count),
                        rx.spacer(),
                    ),
                    style=styles.dashboard_info_box_style,
                ),
                rx.vstack(
                    rx.heading("Closed", size="md"),
                    rx.hstack(
                        rx.icon(
                            tag="close",
                        ),
                        rx.heading(HomeState.projects_closed_count),
                        rx.spacer(),
                    ),
                    style=styles.dashboard_info_box_style,
                ),
            ),
            rx.spacer(min_h="20"),
            rx.hstack(
                rx.heading("Project Title", size="xs", width="20vw"),
                rx.heading("PO Number", size="xs", width="15vw"),
                rx.heading("Customer", size="xs", width="15vw"),
                rx.heading("PO Value", size="xs", width="10vw"),
                rx.heading("Delivery Date", size="xs", width="15vw"),
                rx.heading("Status", size="xs", width="10vw"),
                rx.heading("Action", size="xs", width="15vw", text_align="center"),
                border_bottom_left_radius="10",
                border_bottom_right_radius="10",
                p="2",
                position="sticky",
                top="9.2%",
                z_index="100",
                min_h="50",
                bg=styles.bg_main_color,
            ),
            rx.foreach(HomeState.projects, render_project),
            style=styles.inner_display_style,
            max_w="4xl",
            min_w="4xl",
        ),
        rx.box(
            rx.heading("Next Project Events", size="sm", color=styles.text_color_blue),
            rx.spacer(min_h="5"),
            rx.divider(),
            style=styles.sidebar_style,
        ),
        p="8",
    )


def render_project(project: dict):
    return rx.box(
        rx.hstack(
            rx.text(project["title"], width="20vw"),
            rx.text(project["po_number"], width="15vw"),
            rx.text(project["customer_name"], width="15vw"),
            rx.text(project["po_value"], width="10vw"),
            rx.text(project["po_delivery_date"], width="15vw"),
            rx.text(project["status"], width="10vw"),
            rx.hstack(
                rx.tooltip(
                    rx.icon(
                        tag="view",
                        cursor="pointer",
                        on_click=HomeState.set_selected_project(project),
                    ),
                    label="View",
                ),
                rx.tooltip(
                    rx.icon(
                        tag="copy",
                        cursor="pointer",
                    ),
                    label="Copy",
                ),
                rx.tooltip(
                    rx.icon(
                        tag="edit",
                        cursor="pointer",
                    ),
                    label="Edit",
                ),
                rx.tooltip(
                    rx.icon(
                        tag="delete",
                        cursor="pointer",
                    ),
                    label="Delete",
                ),
                width="15vw",
                justify="center",
            ),
            min_h="100",
        ),
        rx.divider(),
    )


def project_display():
    return rx.hstack(
        rx.box(
            rx.heading("Actions", size="sm"),
            rx.spacer(min_h="2"),
            rx.divider(),
            rx.spacer(min_h="5"),
            rx.link(
                "Update Status",
                on_click=ProjectState.toggle_modal,
                color=styles.accent_color_blue,
            ),
            rx.spacer(min_h="2"),
            style=styles.sidebar_style,
        ),
        rx.box(
            rx.hstack(
                rx.heading(HomeState.selected_project["po_number"], size="md"),
                rx.box(
                    rx.text(
                        HomeState.selected_project["status"],
                        font_size="sm",
                    ),
                    style=styles.status_box_style,
                ),
                rx.spacer(),
            ),
            rx.spacer(min_h="5"),
            rx.text(
                f"{HomeState.selected_project['title']}: {HomeState.selected_project['description']}",
                color="grey",
            ),
            rx.spacer(min_h="5"),
            rx.hstack(
                rx.box(
                    rx.text(
                        HomeState.selected_project["po_number"],
                        font_weight="bold",
                    ),
                    rx.text(
                        "Order #",
                        font_size="sm",
                        color="grey",
                    ),
                    style=styles.info_box_style,
                ),
                rx.box(
                    rx.text(
                        HomeState.selected_project["customer_name"],
                        font_weight="bold",
                    ),
                    rx.text(
                        "Customer",
                        font_size="sm",
                        color="grey",
                    ),
                    style=styles.info_box_style,
                ),
                rx.box(
                    rx.text(
                        HomeState.selected_project["po_issue_date"],
                        font_weight="bold",
                    ),
                    rx.text(
                        "PO Issue Date",
                        font_size="sm",
                        color="grey",
                    ),
                    style=styles.info_box_style,
                ),
                rx.box(
                    rx.text(
                        HomeState.selected_project["po_delivery_date"],
                        font_weight="bold",
                    ),
                    rx.text(
                        "Target Delivery Date",
                        font_size="sm",
                        color="grey",
                    ),
                    style=styles.info_box_style,
                ),
                rx.box(
                    rx.text(
                        HomeState.selected_project["po_value"],
                        font_weight="bold",
                    ),
                    rx.text(
                        "Purchase Order Value",
                        font_size="sm",
                        color="grey",
                    ),
                    style=styles.info_box_style,
                ),
            ),
            rx.spacer(min_h="50"),
            rx.tabs(
                items=[
                    (
                        "Activity",
                        rx.vstack(
                            rx.heading("Milestone 1", size="sm"),
                            rx.heading("Milestone 2", size="sm"),
                            rx.heading("Milestone 3", size="sm"),
                        ),
                    ),
                    (
                        "Documents",
                        rx.vstack(
                            rx.heading("Document 1", size="sm"),
                            rx.heading("Document 2", size="sm"),
                            rx.heading("Document 3", size="sm"),
                        ),
                    ),
                ],
            ),
            style=styles.inner_display_style,
        ),
        p="8",
    )
