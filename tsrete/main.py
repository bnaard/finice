from nicegui import Tailwind, ui

import theme
import rete

# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame():
        ui.label("Homepage")

@ui.page('/tables')
def index_page() -> None:
    with theme.frame():
        ui.label("Tables")

@ui.page('/rete')
def index_page() -> None:
    with theme.frame():
        ui.label("Rete")
        rete.ReteGraph()


ui.run(title='Rete TS Example')

