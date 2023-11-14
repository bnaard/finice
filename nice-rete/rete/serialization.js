
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


export function deserializeNode(data) {
    const { id, label, inputs, outputs, controls } = data;
    const node = new window.Rete.ClassicPreset.Node(label);

    console.log(data)
    console.log(id, label)
    node.id = id;

    if (inputs != null && Object.keys(inputs).length > 0) { 
        Object.entries(inputs).forEach(([key, input]) => {
            const socket = new window.Rete.ClassicPreset.Socket(input.socket.name);
            const inp = new window.Rete.ClassicPreset.Input(socket, input.label);

            inp.id = input.id;

            node.addInput(key, input);
        });
    }

    if (outputs != null && Object.keys(outputs).length > 0) {
        Object.entries(outputs).forEach(([key, output]) => {
            const socket = new window.Rete.ClassicPreset.Socket(output.socket.name);
            const out = new window.Rete.ClassicPreset.Output(socket, output.label);

            out.id = output.id;

            node.addOutput(key, out);
        });
    }

    if (controls != null && Object.keys(controls).length > 0) {
        Object.entries(controls).forEach(([key, control]) => {
            // if (!control) return;

            if (control.__type === "ClassicPreset.InputControl") {
                const ctrl = new window.Rete.ClassicPreset.InputControl(control.type, {
                    initial: control.value,
                    readonly: control.readonly
                });
                node.addControl(key, ctrl);
            }
        });
    }

    return node
}

export async function importGraph(editor, data) {
    for (const nodedata of data.nodes) {
        // { id, label, inputs, outputs, controls } = anode
        var node = deserializeNode(nodedata )
        await editor.addNode(node);
    }
}