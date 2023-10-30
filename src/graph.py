from nicegui import ui

class GraphFrame(ui.element,
              component='graph.js',
              exposed_libraries=['./lib/litegraph.js'],
              extra_libraries=[]):
    pass

