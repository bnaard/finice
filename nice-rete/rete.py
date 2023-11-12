from nicegui import ui, Tailwind
import uuid

class ReteGraph(ui.element, component='rete.js', libraries=[
                'lib/rete/rete.min.js',
                'lib/rete/rete-area-plugin.min.js',
                'lib/rete/rete-connection-plugin.min.js',
                'lib/rete/rete-render-utils.min.js',
                'lib/rete/rete-vue-plugin.min.js',
            ],
            exposed_libraries= ['./rete/*.js']):

    def __init__(self, expand: bool = True) -> None:
        super().__init__()
        if expand:
            expanded = Tailwind().height('screen').width("screen")
            expanded.apply(self)

        self._initGraph()


    def _initGraph(self):
        self._props["graph"] = {
            "nodes": list()
        }


    def addNode(self, label: str = "", nodeId: str = str(uuid.uuid4()) ) -> str:
        if type( self._props["graph"] ) != "<class 'dict'>" or "node" not in self._props["graph"].keys() or type( self._props["graph"] ) != "<class 'list'>": 
            self._initGraph()
        newnode = {
			"id": nodeId,
			"label": label,
			"outputs": {
			},
			"inputs": {
			},
			"controls": {
			}
		}
        self._props["graph"]["nodes"].append(newnode)
        if self.mounted:
            self.run_method('addNode', newnode)


    # def addNode(self, nodeId: str = str(uuid.uuid4()) ) -> str:
    #     self.run_method('addNode', nodeId)
    #     return nodeId

    def update(self) -> None:
        super().update()
    #     # self.run_method('update_chart')

