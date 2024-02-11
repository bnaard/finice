from nicegui import ui


class PrimarySideBar:
    def __init__(self):
        self.sidebar = None
        self.draw()

    def draw(self):
        with ui.left_drawer(top_corner=True, bottom_corner=True, value=False).classes(
            "bg-secondary text-blue-grey-1"
        ) as self.sidebar:
            ui.label("Settings")  # .classes("text-blue-1")
