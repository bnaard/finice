import { LGraph, LGraphCanvas, LiteGraph as lg } from 'litegraph';

export default {
  template: `<div><canvas id='mycanvas' width='1024' height='720' style='border: 1px solid'></canvas></div>`,
  mounted() {
    console.log("Test");
    var graph = new LGraph();

    var canvas = new LGraphCanvas("#mycanvas", graph);
    
    var node_const = lg.createNode("basic/const");
    node_const.pos = [200,200];
    graph.add(node_const);
    node_const.setValue(4.5);
    
    var node_watch = lg.createNode("basic/watch");
    node_watch.pos = [700,200];
    graph.add(node_watch);
    
    node_const.connect(0, node_watch, 0 );
    
    graph.start()
  },
  methods: {
  },
  props: {
  },
};
