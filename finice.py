from nicegui import app, ui

from app.startup import startup

app.on_startup(startup)
ui.run()