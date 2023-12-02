from nicegui import Tailwind, ui

import theme

# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame():
        ui.label("Homepage")
