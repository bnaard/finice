class Editor:
    def __init__(self):
        print("adding editor")
    def __enter__(self):
         print("Entering the context...")
         return self
    def __exit__(self, exc_type, exc_value, exc_tb):
         print("Leaving the context...")
    def addNode(self, name):
         print(f"adding node {name}")


class Node:
    def __init__(self, editor, name):
        self.editor = editor
        self.name = name
        self.editor.addNode(name)

    def __enter__(self):
         print("Entering the Nodecontext...")
         self.y = 99
         return self
    def __exit__(self, exc_type, exc_value, exc_tb):
         print("Leaving the Nodecontext...")
    def addInput(self, name):
         print(f"adding input {name}")


class Input:
    def __init__(self, node, name):
        self.node = node
        self.name = name
        self.node.addInput(name)
     


with Editor() as editor:
    with Node(editor, "TestNode") as testnode:
         Input(testnode, "test input")
    