from nicegui import ui

from theme import Menu
from theme import PrimarySideBar


class Frame(object):
    def __init__(self):
        ui.colors(
            primary="#02153d",
            secondary="#193763",
            accent="#578685",
            dark="#1d1d1d",
            positive="#21BA45",
            negative="#C10015",
            info="#a2c459",
            warning="#e2e5b5",
        )

    def __enter__(self):
        self.draw()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def draw(self):
        self.primary_side_bar = PrimarySideBar()
        with ui.header(elevated=True).style("align-items: center").props("overlay=false padding=xs").classes("q-pa-xs"):
            self.menu = Menu(primary_side_bar=self.primary_side_bar)
        with ui.footer():
            ui.label("FOOTER")
