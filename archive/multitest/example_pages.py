import theme

from nicegui import ui


def create() -> None:

    @ui.page('/a')
    def example_page_a():
        with theme.frame('- Example A -'):
            ui.label('Example A').classes('text-h4 text-grey-8')

    @ui.page('/b/{id}')
    def example_page_b(id: str):
        with theme.frame('- Example B -'):
            ui.label(f'Example B with id {id}').classes('text-h4 text-grey-8')
