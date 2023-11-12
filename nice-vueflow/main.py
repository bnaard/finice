from nicegui import Tailwind, ui

import theme
import vueflow as vf

# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame():
        ui.label("Homepage")

@ui.page('/tables')
def index_page() -> None:
    with theme.frame():
        ui.label("Tables")

@ui.page('/vueflow')
def index_page() -> None:
    with theme.frame():
        ui.label("Vue Flow")
        vf.VueFlowGraph()


smiley = '''
    <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="78" fill="#ffde34" stroke="black" stroke-width="3" />
        <circle cx="80" cy="85" r="8" />
        <circle cx="120" cy="85" r="8" />
        <path d="m60,120 C75,150 125,150 140,120" style="fill:none; stroke:black; stroke-width:8; stroke-linecap:round" />
    </svg>
'''

ui.run(title='Vue FLow Example', uvicorn_reload_includes='*.py, *.html, *.css, *.js, *.vue', favicon=smiley)

