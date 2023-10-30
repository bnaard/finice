<template>
<div class="rete" ref="rete"></div>
</template>


<script>
export default {
  mounted() {
    const socket = new window.Rete.ClassicPreset.Socket("socket");
    const editor = new window.Rete.NodeEditor();
    const area = new window.ReteAreaPlugin.AreaPlugin(this.$refs.rete);
    const connection = new window.ReteConnectionPlugin.ConnectionPlugin();
    const render = new window.ReteVuePlugin.VuePlugin();

    window.ReteAreaPlugin.AreaExtensions.selectableNodes(area, window.ReteAreaPlugin.AreaExtensions.selector(), {
        accumulating: window.ReteAreaPlugin.AreaExtensions.accumulateOnCtrl()
    });

    render.addPreset(window.ReteVuePlugin.Presets.classic.setup());

    connection.addPreset(window.ReteConnectionPlugin.Presets.classic.setup());

    editor.use(area);
    area.use(connection);
    area.use(render);

    window.ReteAreaPlugin.AreaExtensions.simpleNodesOrder(area);

    const a = new window.Rete.ClassicPreset.Node("A");
    a.addControl(
        "a",
        new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
    );
    a.addOutput("a", new window.Rete.ClassicPreset.Output(socket));
    editor.addNode(a);

    const b = new window.Rete.ClassicPreset.Node("B");
    b.addControl(
        "b",
        new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
    );
    b.addInput("b", new window.Rete.ClassicPreset.Input(socket));
    editor.addNode(b);

    area.translate(b.id, { x: 320, y: 0 });

    editor.addConnection(new window.Rete.ClassicPreset.Connection(a, "a", b, "b"));

    window.ReteAreaPlugin.AreaExtensions.zoomAt(area, editor.getNodes());

    return () => area.destroy();

  },
  props: {
  },
};
</script>

<style lang="scss">
body {
    margin: 0;
}
.rete {
    width: 100vw;
    height: 100vh;
}

</style>
    