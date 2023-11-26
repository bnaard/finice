# from nicegui import ui

# class ReteGraph(ui.element,
#               component='rete.js',
#               exposed_libraries=['./lib/rete/rete-area-plugin.min.js', './lib/rete/rete-connection-plugin.min.js', './lib/rete/rete-react-plugin.min.js', './lib/rete/rete-render-utils.min.js', './lib/rete/rete-vue-plugin.min.js', './lib/rete/rete.min.js' ],
#               extra_libraries=[]):
#     pass


from nicegui import ui


class ReteGraph(ui.element, component='rete.js' ):
    pass