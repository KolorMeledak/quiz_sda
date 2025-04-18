import os

# Download https://graphviz.org/download lalu tambahkan env variables PATH
# install graphviz via pip
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

def build_bst_from_list(data):
    root = None
    for num in data:
        root = insert(root, num)
    return root

def save_bst_image(root, output_path):
    bst_graph = visualize_bst(root)
    bst_graph.render(output_path, format="png", cleanup=False) # hasil akan disimpan di 'out/bst_output.png'
    print(f"✅ BST berhasil divisualisasikan! Lihat file '{output_path}.png'")

if __name__ == "__main__":
    input_str = input("Masukkan angka (pisahkan dengan koma): ")
    data = [int(x.strip()) for x in input_str.split(',') if x.strip().isdigit()]

    root = build_bst_from_list(data)

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_PATH = os.path.join(CURRENT_DIR, "out", "bst_output")

    save_bst_image(root, OUTPUT_PATH)
