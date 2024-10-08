from word import Node

def get_height(node: Node):
    if not node:
        return 0
    return node.height

def get_balance(node: Node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(a: Node):
    aL = a.left
    aLR = aL.right
    aL.right=a
    a.left=aLR
    a.height = max(get_height(a.left),get_height(a.right))+1
    aL.height = max(get_height(aL.left),get_height(aL.right))+1
    return aL

def left_rotate(a):
    aR = a.right
    aRL = aR.left
    aR.left=a
    a.right=aRL
    a.height = max(get_height(a.left),get_height(a.right))+1
    aR.height = max(get_height(aR.left),get_height(aR.right))+1
    return aR

def find_min(curLeaf):
    if curLeaf.left is None:
        return curLeaf
    else: 
        return find_min(curLeaf.left)