from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def visualize_bst(root):
    dot = Digraph()
    def add_nodes_edges(node):
        if node is None:
            return
        dot.node(str(id(node)), str(node.val))
        if node.left:
            dot.node(str(id(node.left)), str(node.left.val))
            dot.edge(str(id(node)), str(id(node.left)), label="L")
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(id(node.right)), str(node.right.val))
            dot.edge(str(id(node)), str(id(node.right)), label="R")
            add_nodes_edges(node.right)
    add_nodes_edges(root)
    return dot

data = [155, 142, 85, 176, 78, 36, 32, 59, 37, 169, 38, 55, 62, 68, 49, 69, 91]

root = None
for num in data:
    root = insert(root, num)

bst_graph = visualize_bst(root)
bst_graph.render("bst_output", format="png", cleanup=False)  # hasil akan disimpan di 'bst_output.png'

print("✅ BST berhasil divisualisasikan! Lihat file 'bst_output.png'")
