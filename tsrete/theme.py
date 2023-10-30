from contextlib import contextmanager

from nicegui import ui


@contextmanager
def frame():


    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(
        primary='#02153d',
        secondary='#193763',
        accent='#578685',

        dark='#1d1d1d',

        positive='#21BA45',
        negative='#C10015',
        info='#a2c459',
        warning='#e2e5b5'       
    )
    with ui.header(elevated=True).style("align-items: center").props("overlay=false padding=xs").classes('q-pa-xs'):
        with ui.tabs() as tabs:
            ui.tab('Tables').on( type="click", handler=lambda: ui.open("/tables") )
            ui.tab('Rete').on( type="click", handler=lambda: ui.open("/rete"))
        ui.element("div").style("flex-grow: 1")
        ui.button(on_click=lambda: right_drawer.toggle(), icon='settings').props('flat color=white')
    with ui.right_drawer( top_corner=True, bottom_corner=True, value=False ).classes("bg-secondary text-blue-grey-1") as right_drawer:
        ui.label('Settings') # .classes("text-blue-1")
    with ui.footer():
        ui.label('FOOTER')

    yield
