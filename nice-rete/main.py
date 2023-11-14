from nicegui import Tailwind, ui

import theme
from rete import ReteGraph, Node 

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
        with ReteGraph() as rtg:
            with Node(rtg, "Yay!") as n1:
                pass
                # Input(n1, xxx )
                # Control( n1, zzz )
                # Output(n1, yyy )



ui.run(title='Rete Example')

