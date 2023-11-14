from nicegui import ui, Tailwind
import uuid

class Editor(ui.element, component='rete.js', libraries=[
                'lib/rete/rete.min.js',
                'lib/rete/rete-area-plugin.min.js',
                'lib/rete/rete-connection-plugin.min.js',
                'lib/rete/rete-render-utils.min.js',
                'lib/rete/rete-vue-plugin.min.js',
            ],
            exposed_libraries= ['./rete/*.js']):

    def __init__(self, expand: bool = True) -> None:
        super().__init__()
        self._props["ismounted"] = False
        if expand:
            expanded = Tailwind().height('screen').width("screen")
            expanded.apply(self)
        self._props["graph"] = {}

    def update(self) -> None:
        super().update()
    #     # self.run_method('update_chart')



class Graph:
    def __init__(self) -> None:
        super().__init__()
        self._initGraph()

    def _initGraph(self):
        self.data = {
            "nodes": list()
        }

    def addNode(self, label: str = "", nodeId: str = str(uuid.uuid4()) ) -> str:
        if type( self.data ) != "<class 'dict'>" or "node" not in self.data.keys() or type( self.data ) != "<class 'list'>": 
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
        self.data["nodes"].append(newnode)
        return nodeId


    # def _addNode(self, newnode : Node = None ) -> None:
    #     if type( self._props["graph"] ) != "<class 'dict'>" or "node" not in self._props["graph"].keys() or type( self._props["graph"] ) != "<class 'list'>": 
    #         self._initGraph()
    #     self._props["graph"]["nodes"].append(newnode.data)
    #     if self._props["ismounted"]:
    #         self.run_method('addNode', newnode.data)


# class Node:
#     def __init__(self, graph: ReteGraph = None, label: str = "", nodeId: str = str(uuid.uuid4())) -> None:
#         if graph is None:
#             raise ValueError()
        
#         self._data = {
# 			"id": nodeId,
# 			"label": label,
# 			"outputs": {
# 			},
# 			"inputs": {
# 			},
# 			"controls": {
# 			}
# 		}
#         graph._addNode(self)



#     def __enter__(self):
#         pass

#     def __exit__(self):
#         pass

#     @property
#     def data(self):
#         return self._data

#     @data.setter
#     def data(self, value):
#         self._data = value
    