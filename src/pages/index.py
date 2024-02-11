from nicegui import ui

from theme import Frame

@ui.page('/')
def index_page() -> None:
    with Frame():
        ui.label("Homepage")
