# Trees 

# Pre - order traversal

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def PreorderTraversal(node):           #tarversal operations
    if node is None:
        return
    print(node.data,end = ", ")
    PreorderTraversal(node.left)
    PreorderTraversal(node.right)

def InorderTraversal(node):
    if node is None:
        return
    InorderTraversal(node.left)
    print(node.data,end=",")
    InorderTraversal(node.right)

def PostorderTraversal(node):
    if node is None:
        return
    PostorderTraversal(node.left)
    PostorderTraversal(node.right)
    print(node.data,end=" , ")

def Search(node,target):                # Binary search tree
    if node is None:
        return
    elif node.data == target:
        return node
    elif target < node.data:
        return Search(node.left,target)
    else:
        return Search(node.right, target)
    

def InsertNode(node,data):                  #Insert tree
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = InsertNode(node.left,data)
        elif data > node.data:
            node.right = InsertNode(node.right,data)
    return node

def delete(node, data):                     #Delete tree
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)

    return node
        
root = TreeNode("V")
nodeA = TreeNode("A")
nodeB = TreeNode("I")
nodeC =TreeNode("H")
nodeD = TreeNode("A")
nodeE = TreeNode("V")
nodeF =TreeNode("B")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

PreorderTraversal(root)

InorderTraversal(root)

PostorderTraversal(root)

result = Search(root, "B")

InsertNode(root,"S")

delete(root,"V")

print(result)
print("DAta : ",root.right.left.data)