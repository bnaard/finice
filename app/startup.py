from nicegui import ui


def hello() -> None:
    ui.notify("Hello World!")


def startup() -> None:
    @ui.page("/")
    def index() -> None:
        ui.button("Click me", on_click=hello)
