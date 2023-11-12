from nicegui import ui, Tailwind
import uuid

class VueFlowGraph(ui.element, component='vueflow.vue', libraries=[
                'lib/vueflow/vue-flow-core.iife.min.js',
            ]):

    def __init__(self, expand: bool = True) -> None:
        super().__init__()
        # ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/@vue-flow/core@1.26.0/dist/vue-flow-core.iife.min.js"></script>')

        if expand:
            expanded = Tailwind().height('screen').width("screen")
            expanded.apply(self)
        self._props['elements'] = [
            { "id": "1", "type": "input", "label": 'Node 1', "position": { "x": 250, "y": 5 } },
            { "id": "2", "label": 'Node 2', "position": { "x": 100, "y": 100 } },
            { "id": "3", "type": "output", "label": 'Node 3', "position": { "x": 400, "y": 200 } },
            { "id": "e1-3", "source": "1", "target": "3" },
            { "id": "e1-2", "source": "1", "target": "2", "animated": True }
        ]
