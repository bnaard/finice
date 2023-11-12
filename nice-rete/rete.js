/* <template>
    <div class="retegraph" ref="rete"></div>
</template>




<script> */

import { createNode } from "nicenode";
import { exportGraph, importGraph, deserializeNode } from "serialization";


export default {

    template: '<div class="retegraph" ref="rete"></div>',

    async mounted() {
        this.socket = new window.Rete.ClassicPreset.Socket("socket");
        this.editor = new window.Rete.NodeEditor();
        this.area = new window.ReteAreaPlugin.AreaPlugin(this.$refs.rete);
        this.connection = new window.ReteConnectionPlugin.ConnectionPlugin();
        this.render = new window.ReteVuePlugin.VuePlugin();

        window.ReteAreaPlugin.AreaExtensions.selectableNodes(this.area, window.ReteAreaPlugin.AreaExtensions.selector(), {
            accumulating: window.ReteAreaPlugin.AreaExtensions.accumulateOnCtrl()
        });

        this.render.addPreset(window.ReteVuePlugin.Presets.classic.setup());

        this.connection.addPreset(window.ReteConnectionPlugin.Presets.classic.setup());

        this.editor.use(this.area);
        this.area.use(this.connection);
        this.area.use(this.render);

        window.ReteAreaPlugin.AreaExtensions.simpleNodesOrder(this.area);

        const x = createNode("X", this.socket); 
        await this.editor.addNode(x);
        await this.area.translate(x.id, { x: 320, y: 50 });


        const a = new window.Rete.ClassicPreset.Node("A");
        a.addControl(
            "a",
            new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
        );
        a.addOutput("a", new window.Rete.ClassicPreset.Output(this.socket));
        await this.editor.addNode(a);

        const b = new window.Rete.ClassicPreset.Node("B");
        b.addControl(
            "b",
            new window.Rete.ClassicPreset.InputControl("text", { initial: "hello" })
        );
        b.addInput("b", new window.Rete.ClassicPreset.Input(this.socket));
        await this.editor.addNode(b);

        await this.area.translate(b.id, { x: 420, y: 100 });

        await this.editor.addConnection(new window.Rete.ClassicPreset.Connection(a, "a", b, "b"));

        window.ReteAreaPlugin.AreaExtensions.zoomAt(this.area, this.editor.getNodes());

    },
    beforeDestroy() {
        this.area.destroy();
    },
    beforeUnmount() {
        this.area.destroy();
    },
    props: {
        graph: Object
    },
    methods: {
        update_chart() {
            //   convertDynamicProperties(this.options, true);
            //   this.chart.setOption(this.options);
        },
        async addNode(nodedict) {
            this.$nextTick( async function() {
                const node = deserializeNode(nodedict)
                await this.editor.addNode(node);
            });
        },
        // async addNode(nodeId) {
        //     this.$nextTick( async function() {
        //         const a = new window.Rete.ClassicPreset.Node(nodeId);
        //         await this.editor.addNode(a);
        //     });
        // },
        addInput(nodeId, inputId) {
            const anode = this.editor.getNode(nodeId)
            anode.addInput(inputId, new window.Rete.ClassicPreset.Input(this.socket));
        }
    }

};


// </script>

