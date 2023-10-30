// import { NodeEditor, ClassicPreset } from "rete";

// import { AreaPlugin, AreaExtensions } from "rete-area-plugin";
// import {
//   ConnectionPlugin,
//   Presets as ConnectionPresets
// } from "rete-connection-plugin";
// import { VuePlugin, Presets } from "rete-vue-plugin";

// const ClassicPreset = window.Rete.ClassicPreset;
// const NodeEditor = window.Rete.NodeEditor;


export default {
  template: `<div><div class="rete" ref="rete"></div></div>`,
  mounted() {
    console.log("Rete Test");
    const socket = new window.Rete.ClassicPreset.Socket("socket");

    const editor = new window.Rete.NodeEditor();
    const area = new window.Rete.AreaPlugin('<div class="rete" ref="rete"></div>');
    const connection = new window.Rete.ConnectionPlugin();
    const render = new window.Rete.VuePlugin();
  
    window.Rete.AreaExtensions.selectableNodes(area, window.Rete.AreaExtensions.selector(), {
      accumulating: window.Rete.AreaExtensions.accumulateOnCtrl()
    })
  
    render.addPreset(window.Rete.Presets.classic.setup())
  
    connection.addPreset(window.Rete.ConnectionPresets.classic.setup())
  
    editor.use(area)
    area.use(connection)
    area.use(render)
  
    window.Rete.AreaExtensions.simpleNodesOrder(area)
  
    const a = new window.Rete.ClassicPreset.Node("A")
    a.addControl(
      "a",
      new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
    )
    a.addOutput("a", new window.Rete.ClassicPreset.Output(socket))
    // await editor.addNode(a)
    editor.addNode(a)
  
    const b = new window.Rete.ClassicPreset.Node("B")
    b.addControl(
      "b",
      new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
    )
    b.addInput("b", new window.Rete.ClassicPreset.Input(socket))
    // await editor.addNode(b)
    editor.addNode(b)
  
    // await area.translate(b.id, { x: 320, y: 0 })
    area.translate(b.id, { x: 320, y: 0 })
  
    // await editor.addConnection(new window.Rete.ClassicPreset.Connection(a, "a", b, "b"))
    editor.addConnection(new window.Rete.ClassicPreset.Connection(a, "a", b, "b"))
  
    window.Rete.AreaExtensions.zoomAt(area, editor.getNodes())
  
    return () => area.destroy()
  },
  methods: {
  },
  props: {
  },
};
