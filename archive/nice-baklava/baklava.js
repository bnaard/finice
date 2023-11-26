export default {
  template: `<div class="baklavaeditoridentifier"></div>`,

  mounted() {
    const bjs = window.BaklavaJS.BaklavaJS;
    const viewModel = bjs.createBaklava(document.querySelectorAll(".baklavaeditoridentifier")[0]);
    const TestNode = bjs.Core.defineNode({
        type: "TestNode",
        inputs: {
            a: () => new bjs.RendererVue.TextInputInterface("Hello", "world"),
        },
        outputs: {
            b: () => new bjs.RendererVue.TextInputInterface("Hello", "world"),
        },
    });
    viewModel.editor.registerNodeType(TestNode);
  },
  props: {
    options: Object,
    elements: Object
  },
  setup(props) {
    console.log(props.elements)
  },
  methods: {
    onRemoveNode() {
      elements.value.pop()
    }
  }
};
