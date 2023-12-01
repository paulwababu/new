import reflex as rx

bg_main_color = "#f5f5f5"
bg_seconday_color = "#fff"

border_color = "#fff3"

accent_light = "#6649D8"
accent_color = "#5535d4"
accent_dark = "#4c2db3"
accent_greyish = "#52507F"

accent_color_blue = "#3B49DF"

icon_color = "#979797"

text_color = "#424242"
text_color_blue = "#012970"
shadow_light = "rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;"
shadow = "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;"

message_style = dict(display="inline-block", p="4", border_radius="xl", max_w="30em")

navbar_style = dict(
    bg=bg_seconday_color,
    backdrop_filter="auto",
    backdrop_blur="lg",
    p="4",
    border_bottom=f"1px solid {border_color}",
    position="sticky",
    top="0",
    z_index="101",
)

page_style = dict(
    bg=bg_main_color,
    color=text_color,
    min_h="100vh",
    align_items="stretch",
    spacing="0",
)

main_button_style = dict(
    bg=accent_color,
    color="#ffffff",
    px="4",
    py="2",
    h="auto",
    w="100%",
    _hover={"bg": accent_dark},
)

input_style = dict(
    bg=bg_seconday_color,
    border_color=border_color,
    border_width="1px",
    p="4",
)

icon_style = dict(
    font_size="md",
    color=icon_color,
    _hover=dict(color=text_color),
    cursor="pointer",
    w="8",
)

sidedrawer_style = dict(
    border="double 1px transparent;",
    border_radius="10px;",
    background_image=f"linear-gradient({bg_main_color}, {bg_main_color}), radial-gradient(circle at top left, {accent_color},{accent_dark});",
    background_origin="border-box;",
    background_clip="padding-box, border-box;",
    p="2",
    _hover=dict(
        background_image=f"linear-gradient({bg_main_color}, {bg_main_color}), radial-gradient(circle at top left, {accent_color},{accent_light});",
    ),
)

sidebar_style = dict(
    border_radius="10",
    min_h="60vh",
    width="100vw",
    bg=bg_seconday_color,
    p="8",
    align_self="start",
    position="sticky",
    top="12%",
)

info_box_style = dict(
    border=f"1px dashed grey",
    px="5",
    py="5",
    border_radius="5",
)

status_box_style = dict(
    bg="#FFECDF",
    px="4",
    py="1",
    border_radius="5px",
    color="#FF771E",
)

inner_display_style = dict(
    flex="1",
    min_height="100vh",
    max_w="6xl",
    min_w="6xl",
    p="8",
    bg=bg_seconday_color,
    border_radius="10",
)

dashboard_info_box_style = dict(
    min_h="100",
    min_w="200",
    bg=bg_seconday_color,
    border_radius="10",
    border=f"1px solid {accent_color_blue}",
    p="5",
)

sans = "Instrument Sans"
nav_search_style = dict(
    color="#342E5C",
    # font_family=sans,
    font_weight="500",
)

base_style = {
    rx.Avatar: {
        "shadow": shadow,
        "color": text_color,
        "bg": icon_color,
    },
    rx.Button: {
        "shadow": shadow,
        "color": text_color,
        "_hover": {
            "bg": accent_dark,
        },
    },
    rx.Menu: {
        "bg": bg_main_color,
        "border": f"red",
    },
    rx.MenuList: {
        "bg": bg_main_color,
        "border": f"1.5px solid {bg_seconday_color}",
    },
    rx.MenuDivider: {
        "border": f"1px solid {bg_seconday_color}",
    },
    rx.MenuItem: {
        "bg": bg_main_color,
        "color": text_color,
    },
    rx.DrawerContent: {
        "bg": bg_main_color,
        "color": text_color,
        # "opacity": "0.9",
    },
    rx.Hstack: {
        "align_items": "center",
        "justify_content": "space-between",
    },
    rx.Vstack: {
        "align_items": "stretch",
        "justify_content": "space-between",
    },
}
