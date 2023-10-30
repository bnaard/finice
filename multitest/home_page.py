from nicegui import ui
from rete import ReteGraph
from workaround import Workaround


def content() -> None:
    ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')
    Workaround()
    ReteGraph()
