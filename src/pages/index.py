from nicegui import ui

from theme import Frame, PrimarySideBar

@ui.page('/')
def index_page() -> None:
    with PrimarySideBar() as primary_side_bar:
        ui.label("Explorer")
    with Frame( primary_side_bar= primary_side_bar):
        ui.label("Homepage")
