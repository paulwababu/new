import reflex as rx
from zabunifund.state import CustomersState, HomeState, ProjectState
from zabunifund import styles


def add_project_modal() -> rx.Component:
    """A modal to submit a new project."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.form(
                    rx.modal_header(
                        rx.hstack(
                            rx.text("Submit New Project"),
                            rx.icon(
                                tag="close",
                                font_size="sm",
                                on_click=HomeState.toggle_modal,
                                style=styles.icon_style,
                            ),
                            align_items="center",
                            justify_content="space-between",
                        )
                    ),
                    rx.modal_body(
                        rx.hstack(
                            rx.input(
                                placeholder="Project Title",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="title",
                                is_required=True,
                            ),
                        ),
                        rx.hstack(
                            rx.select(
                                HomeState.project_types,
                                placeholder="Select Project Type",
                                # default_value=IndexState.project_types[0],
                                color_schemes="twitter",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": "#ECECEC"},
                                id="ptype",
                                is_required=True,
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.select(
                                HomeState.list_of_customer_names,
                                placeholder="Select Customer",
                                color_schemes="twitter",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="customer",
                                is_required=True,
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.text_area(
                                placeholder="Project Description",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="description",
                                is_required=True,
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Purchase Order Number",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="po_number",
                                is_required=True,
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    "Order Issue Date",
                                    font_size="xs",
                                    font_weight="bold",
                                ),
                                rx.input(
                                    # placeholder="Order Issue Date",
                                    bg=styles.bg_seconday_color,
                                    border_color="#fff3",
                                    _placeholder={"color": styles.text_color},
                                    type_="date",
                                    id="po_issue_date",
                                    is_required=True,
                                ),
                            ),
                            rx.vstack(
                                rx.text(
                                    "Order Delivery Date",
                                    font_size="xs",
                                    font_weight="bold",
                                ),
                                rx.input(
                                    placeholder="Order Delivery Date",
                                    bg=styles.bg_seconday_color,
                                    border_color="#fff3",
                                    _placeholder={"color": styles.text_color},
                                    id="po_delivery_date",
                                    type_="date",
                                    is_required=True,
                                ),
                            ),
                            margin_top="20px",
                            justify="space-between",
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Purchase Order Value",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                type_="number",
                                id="po_value",
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.select(
                                HomeState.currencies,
                                placeholder="Select Currency",
                                color_schemes="twitter",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="po_currency",
                            ),
                            margin_top="20px",
                        ),
                    ),
                    rx.modal_footer(
                        rx.button(
                            "Save Draft",
                            bg="#5535d4",
                            color="#fff",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            type_="submit",
                        ),
                    ),
                    on_submit=HomeState.handle_project_submit,
                ),
                bg=styles.bg_main_color,
                color=styles.text_color,
            ),
        ),
        is_open=HomeState.modal_open,
        size="lg",
    )


def add_customer_modal() -> rx.Component:
    """A modal to save a new customer."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.form(
                    rx.modal_header(
                        rx.hstack(
                            rx.text("Save New Customer"),
                            rx.icon(
                                tag="close",
                                font_size="sm",
                                on_click=HomeState.toggle_modal,
                                style=styles.icon_style,
                            ),
                            align_items="center",
                            justify_content="space-between",
                        )
                    ),
                    rx.modal_body(
                        rx.hstack(
                            rx.input(
                                placeholder="Organization",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="organization",
                                is_required=True,
                            ),
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Contact Name",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="contact_name",
                                is_required=True,
                            ),
                            margin_top="20px",
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Contact Email",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="contact_email",
                            ),
                            margin_top="20px",
                        ),
                    ),
                    rx.modal_footer(
                        rx.button(
                            "Save",
                            bg="#5535d4",
                            color="#fff",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            type_="submit",
                        ),
                    ),
                    # on_submit=CustomerState.handle_project_submit,
                ),
                bg=styles.bg_main_color,
                color=styles.text_color,
            ),
        ),
        is_open=CustomersState.modal_open,
        size="lg",
    )


def update_status_modal() -> rx.Component:
    """A modal to update project status."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.form(
                    rx.modal_header(
                        rx.hstack(
                            rx.text("Update Status"),
                            rx.icon(
                                tag="close",
                                font_size="sm",
                                on_click=HomeState.toggle_modal,
                                style=styles.icon_style,
                            ),
                            align_items="center",
                            justify_content="space-between",
                        )
                    ),
                    rx.modal_body(
                        rx.hstack(
                            rx.select(
                                HomeState.project_status_commands,
                                placeholder="Update Status",
                                color_schemes="twitter",
                                bg=styles.bg_seconday_color,
                                border_color="#fff3",
                                _placeholder={"color": styles.text_color},
                                id="status",
                                is_required=True,
                            ),
                        ),
                    ),
                    rx.modal_footer(
                        rx.button(
                            "Close",
                            bg=styles.accent_greyish,
                            color="#fff",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            on_click=ProjectState.toggle_modal,
                        ),
                        rx.spacer(max_w="5"),
                        rx.button(
                            "Update",
                            bg="#5535d4",
                            color="#fff",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            type_="submit",
                        ),
                    ),
                    # on_submit=CustomerState.handle_project_submit,
                ),
                bg=styles.bg_main_color,
                color=styles.text_color,
            ),
        ),
        is_open=ProjectState.modal_open,
        size="lg",
    )
