

from nicegui import Tailwind, ui, APIRouter, app

from router import Router


# apirouter = APIRouter(prefix='/three')

# @apirouter.page('/{id}')
# def page(id: str):
#     ui.label(f'This is content on /three with id {id}')

# spa_router = Router()

# from spa_api_router import SPAAPIRouter

# spa_router1 = SPAAPIRouter()  # (prefix='/test')


# @spa_router1.spapage('/one')
# def show_one():
#     ui.label('Content One').classes('text-2xl')
#     [ui.label(f'Line {i}') for i in range(100)]


# @spa_router1.spapage('/two')
# def show_two():
#     ui.label('Content Two').classes('text-2xl')


# @spa_router1.spapage('/three/{id}')
# def show_three( id: str = "" ):
#     ui.label(f'Content Three with id {id}').classes('text-2xl')



@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main():
    router = Router()

    @router.add('/')
    def show_one():
        ui.label('Content One').classes('text-2xl')
        [ui.label(f'Line {i}') for i in range(100)]

    @router.add('/two')
    def show_two():
        ui.label('Content Two').classes('text-2xl')
 

    @router.add('/three')
    def show_three(id:str = ""):
        ui.label(f'Content Three with id {id}').classes('text-2xl')
  
    # adding some navigation buttons to switch between the different pages
    with ui.header(elevated=True).style("align-items: center").props("overlay=false padding=xs").classes('q-pa-xs'):
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.link("test", "/one")
        ui.button('FINICE', on_click=lambda: router.open(show_one)).props("flat color=standard no-caps padding=xs")  # .classes('w-32')
        ui.button('Two', on_click=lambda: router.open(show_two)).props("flat color=standard no-caps padding=xs")  # .classes('w-32')
        ui.button('Three', on_click=lambda: router.open(show_three)).props("flat color=standard no-caps padding=xs")  # .classes('w-32')
        with ui.tabs() as tabs:
            ui.tab('A').on( type="click", handler=lambda: router.open(show_one) )
            ui.tab('B').on( type="click", handler=lambda: router.open(show_two))
            ui.tab('C').on( type="click", handler=lambda: router.open(show_three))

        ui.element("div").style("flex-grow: 1")
        ui.label('Right?')
    with ui.left_drawer(fixed=False).style('background-color: #d7e3f4') as left_drawer: 
        ui.label('LEFT DRAWER')
    with ui.footer():
        ui.label('FOOTER')
 
    # this places the content which should be displayed
    router.frame().classes('w-full') # p-4 bg-gray-100')
    # spa_router1.frame().classes('w-full') # p-4 bg-gray-100')


# app.include_router(spa_router1)
ui.run()
