from nicegui import ui

from theme.primary_side_bar import PrimarySideBar

class Menu:
    def __init__( self, primary_side_bar: PrimarySideBar = None ):
        self.primary_side_bar = primary_side_bar
        self.draw()

    def draw(self):
        ui.button( "Finice", on_click=lambda: ui.open("/a") ).props('flat color=white')
        with ui.tabs() as self.tabs:
            ui.tab('Tab 1').on( type="click", handler=lambda: ui.open("/a") )
            ui.tab('Tab 2').on( type="click", handler=lambda: ui.open("/b"))
        ui.space()
        if self.primary_side_bar is not None:
            ui.button(on_click=lambda: self.primary_side_bar.sidebar.toggle(), icon='settings').props('flat color=white')

