from nicegui import ui


class PrimarySideBar:
    def __init__(self):
        self.sidebar = None

    def __enter__(self):
        self.sidebar = ui.left_drawer(top_corner=True, bottom_corner=True, value=False).classes(
            "bg-secondary text-blue-grey-1"
        )
        self.sidebar.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sidebar.__exit__(exc_type, exc_value, traceback)