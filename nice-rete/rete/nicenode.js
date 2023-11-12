
export function createNode(name, socket) {
    const a = new window.Rete.ClassicPreset.Node(name);
    a.addControl(
        name,
        new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
    );
    a.addOutput(name, new window.Rete.ClassicPreset.Output(socket));
    return a;
}
