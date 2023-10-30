from nicegui import ui

class ReteGraph(ui.element, component='rete.vue', libraries=[
                'lib/rete/rete.min.js',
                'lib/rete/rete-area-plugin.min.js',
                'lib/rete/rete-connection-plugin.min.js',
                'lib/rete/rete-render-utils.min.js',
                'lib/rete/rete-vue-plugin.min.js',
            ]):
    def __init__(self) -> None:
        super().__init__()
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete/rete.min.js"></script>')
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete-area-plugin/rete-area-plugin.min.js"></script>')
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete-connection-plugin/rete-connection-plugin.min.js"></script>')
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete-render-utils/rete-render-utils.min.js"></script>')
        # # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete-react-plugin/rete-react-plugin.min.js"></script>')
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/rete-vue-plugin/rete-vue-plugin.min.js"></script>')


