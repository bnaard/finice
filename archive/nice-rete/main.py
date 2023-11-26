from nicegui import Tailwind, ui

import theme
from rete import Graph, Editor 

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
        # ui.button('Add Node', on_click=lambda: rtg.addNode() )
        rtg = Graph()
        n1 = rtg.add_node("Yay!")
        rtg.add_input(n1, "input")
        Editor().show_graph(rtg)



ui.run(title='Rete Example')

