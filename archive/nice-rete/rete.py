from nicegui import ui, Tailwind
import uuid
from enum import Enum, auto



class ControlsTypes(Enum):
    INPUT = auto()
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}'

class InputControlsTypes(Enum):
    TEXT = auto()
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}'



class Graph:
    def __init__(self) -> None:
        super().__init__()
        self._init_graph()

    def _init_graph(self):
        self.data = {
            "nodes": {}
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def add_node(self, label: str = "", node_id: str = str(uuid.uuid4()) ) -> str:
        if not self._check_schema_graph(): 
            raise ValueError
        self.data["nodes"][node_id] = self._create_node(label)
        return node_id


    def add_input(self, node_id, label: str = "", socket: str = "", port_id: str = str(uuid.uuid4())) -> str:
        if not self._check_schema_nodes(node_id):
            raise ValueError
        self.data["nodes"][node_id]["inputs"][port_id] = self._create_port(label, socket)
        return port_id

    def add_output(self, node_id, label: str = "", socket: str = "", port_id: str = str(uuid.uuid4())) -> str:
        if not self._check_schema_nodes(node_id):
            raise ValueError
        self.data["nodes"][node_id]["outputs"][port_id] = self._create_port(label, socket)
        return port_id

    def add_input_control(self, node_id, 
                          input_type: InputControlsTypes = InputControlsTypes.TEXT,
                          value : str = "",
                          readonly: bool = False,
                          control_id: str = str(uuid.uuid4()) ) -> str:
        if not self._check_schema_nodes(node_id):
            raise ValueError
        self.data["nodes"][node_id]["controls"][control_id] = self._create_input_control(input_type, value, readonly)
        return control_id



    def _check_schema_graph(self) -> bool:
        return type( self.data ) is dict and \
            "nodes" in self.data.keys() and \
            type( self.data["nodes"] ) is dict
    
    def _check_schema_nodes(self, node_id) -> bool:
        return self._check_schema_graph() and\
            node_id in self.data["nodes"].keys() and\
            type( self.data["nodes"][node_id]) is dict and\
            "inputs" in self.data["nodes"][node_id].keys() and\
            "outputs" in self.data["nodes"][node_id].keys() and\
            "controls" in self.data["nodes"][node_id].keys()
            

    def _create_node(self, label: str = "") -> None:
        return {
            "label": label,
            "inputs": {},
            "outputs": {},
            "controls": {}
        }
    
    def _create_port(self, label: str = "", socket: str = "") -> None:
        return {
            "label": label,
            "socket": {
                "name": socket
            }
        }
    
    def _create_input_control(self, input_type: InputControlsTypes = InputControlsTypes.TEXT, value : str = "", readonly: bool = False) -> None:
        return {
            "control_type": str(ControlsTypes.INPUT),
            "input_type": str(input_type),
            "value": value,
            "readonly": readonly
        }
    


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

    def show_graph(self, graph: Graph) -> None:
        self._props["graph"] = graph.data 