
function serializePort(port) {
    return {
        id: port.id,
        label: port.label,
        socket: {
            name: port.socket.name
        }
    };
}

function serializeControl(control) {
    if (control instanceof window.Rete.ClassicPreset.InputControl) {
        return serializeClassicPresetInputControl(control)
    }
    return null;
}

function serializeClassicPresetInputControl(control) {
    return {
        __type: "ClassicPreset.InputControl",
        id: control.id,
        readonly: control.readonly,
        type: control.type,
        value: control.value
    };
}

// TODO Change data structure
export async function exportGraph(editor) {
    const data = { nodes: [] };
    const nodes = editor.getNodes();

    for (const node of nodes) {
        const inputsEntries = Object.entries(node.inputs).map(([key, input]) => {
            return [key, input && serializePort(input)];
        });
        const outputsEntries = Object.entries(node.outputs).map(([key, output]) => {
            return [key, output && serializePort(output)];
        });
        const controlsEntries = Object.entries(node.controls).map(
            ([key, control]) => {
                return [key, control && serializeControl(control)];
            }
        );

        data.nodes.push({
            id: node.id,
            label: node.label,
            outputs: Object.fromEntries(outputsEntries),
            inputs: Object.fromEntries(inputsEntries),
            controls: Object.fromEntries(controlsEntries)
        });
    }

    return data;
}


export function deserializeNode(node_id, data) {
    const { label, inputs, outputs, controls } = data;
    const node = new window.Rete.ClassicPreset.Node(label);

    console.log(data)
    console.log(node_id, label)
    node.id = node_id;

    if (inputs != null && Object.keys(inputs).length > 0) { 
        Object.entries(inputs).forEach(([input_id, input_data]) => {
            const socket = new window.Rete.ClassicPreset.Socket(input_data.socket.name);
            const inp = new window.Rete.ClassicPreset.Input(socket, input_data.label);

            inp.id = input_id;

            node.addInput("port", inp);
        });
    }

    if (outputs != null && Object.keys(outputs).length > 0) { 
        Object.entries(outputs).forEach(([output_id, output_data]) => {
            const socket = new window.Rete.ClassicPreset.Socket(output_data.socket.name);
            const outp = new window.Rete.ClassicPreset.Output(socket, output_data.label);

            outp.id = output_id;

            node.addOutput("port", outp);
        });
    }

    if (controls != null && Object.keys(controls).length > 0) {
        Object.entries(controls).forEach(([control_id, control_data]) => {
            if (control_data.control_type === "INPUT") {
                const ctrl = new window.Rete.ClassicPreset.InputControl(control_data._input_type, {
                    initial: control_data.value,
                    readonly: control_data.readonly
                });
                node.addControl("control", ctrl);
            }
        });
    }

    return node
}


async function importNode(editor, node_id, node_data) {
    var node = deserializeNode(node_id, node_data)
    await editor.addNode(node);
}

export async function importGraph(editor, data) {
    Object.entries(data.nodes).forEach(([node_id, node_data]) => {
        importNode(editor, node_id, node_data);
    });
}