
# Integration of LiteGraph to NiceGui

1. Get `litegraph.js` from https://github.com/jagenjo/litegraph.js
2. Add `litegraph.js` to project source directory
3. Edit `litegraph.js`
    - Replace all occurences of `})(this)` with `})(window)` (executing in vue context does not provide the global context required by litegraph) 
    - Search for the following code and comment out.
    ```javascript
    if (typeof exports != "undefined") {
        exports.LiteGraph = window.LiteGraph;
        exports.LGraph = this.LGraph;
        exports.LLink = this.LLink;
        exports.LGraphNode = this.LGraphNode;
        exports.LGraphGroup = this.LGraphGroup;
        exports.DragAndScale = this.DragAndScale;
        exports.LGraphCanvas = this.LGraphCanvas;
        exports.ContextMenu = this.ContextMenu;
    }
    ```
    - add the following code:
    ```javascript
    export let LiteGraph = window.LiteGraph;
    export let LGraph = window.LGraph;
    export let LGraphCanvas = window.LGraphCanvas;
    export let LLink = window.LLink;
    export let LGraphNode = window.LGraphNode;
    export let LGraphGroup = window.LGraphGroup;
    export let DragAndScale = window.DragAndScale;
    export let ContextMenu = window.ContextMenu;
    ```
4. Create `graph.js` with the following test-content:
```javascript

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
```

5. Create `graph.py` with the following content:
```python
from nicegui import ui

class GraphFrame(ui.element,
              component='graph.js',
              exposed_libraries=['./lib/litegraph.js'],
              extra_libraries=[]):
    pass
```    

6. Use like this:
```python
from graph import GraphFrame

ui.label('Graph').classes('text-2xl')
GraphFrame()
 
ui.run()
```
