class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)

if __name__ == "__main__":
    raw_input = input("Masukkan angka-angka (pisahkan dengan koma): ")
    try:
        data = [int(x.strip()) for x in raw_input.split(',') if x.strip()]
    except ValueError:
        print("⚠️ Input harus berupa angka yang dipisahkan koma.")
        exit()

    bst_root = None
    for num in data:
        bst_root = insert(bst_root, num)

    pre, ino, post = [], [], []
    preorder(bst_root, pre)
    inorder(bst_root, ino)
    postorder(bst_root, post)

    print("a) Preorder Traversal :", pre)
    print("b) Inorder Traversal  :", ino)
    print("c) Postorder Traversal:", post)
