class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None




def preorder(node):
    if node == None:
        return
    print(node.data, end = " ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end = " ")
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = " ")


arr = ['a','b','c','d','e']



node = TreeNode()
node.data = arr[0]
root = node

current = root
for data in arr[1:]:
    node = TreeNode()
    node.data = data
    while True:
        if current.data > node.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        elif current.data < node.data:
            if current.right == None:
                current.right = node
                break
            current = current.right
        else:
            print("현재노드와 동일한 값")
            break


preorder(root)
print()
inorder(root)
print()
postorder(root)
