from word import Node
from word import compare
import avl

def insert(root: Node, w: str):
    # bst insert
    if not root:
        return Node(w)
    elif compare(w,root.word)==-1:
        root.left = insert(root.left,w)
    elif compare(w,root.word)>=0:
        root.right = insert(root.right,w)
    root.height = 1 + max(avl.get_height(root.left), avl.get_height(root.right))
    # avl rotation 
    b = avl.get_balance(root)
    #LL
    if b > 1 and compare(w,root.left.word)==-1:
        return avl.right_rotate(root)
    # RR
    if b < -1 and compare(w,root.right.word)==1: 
        return avl.left_rotate(root)
    # LR
    if b > 1 and compare(w,root.left.word)==1:
        root.left = avl.left_rotate(root.left)
        return avl.right_rotate(root)
    # RL
    if b < -1 and compare(w,root.right.word)==-1:
        root.right = avl.right_rotate(root.right)
        return avl.left_rotate(root)
    return root

def delete(root, w):
    #bst
    if root is None:
        return root
    elif compare(root.word,w)==1:
        root.left = delete(root.left,w)
    elif compare(root.word,w)==-1:
        root.right = delete(root.right,w)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left 
        else:
            replace = avl.find_min(root.right)
            root.word = replace.word
            root.right = delete(root.right,replace.word)
    #avl
    if root is None:
        return root
    root.height = max(avl.get_height(root.left),avl.get_height(root.right))+1
    b=avl.get_balance(root)
    # LL
    if b > 1 and avl.get_balance(root.left) >= 0:
        return avl.right_rotate(root)
    # LR
    if b > 1 and avl.get_balance(root.left) < 0:
        root.left = avl.left_rotate(root.left)
        return avl.right_rotate(root)
    # RR
    if b < -1 and avl.get_balance(root.right) <= 0:
        return avl.left_rotate(root)
    # RL
    if b < -1 and avl.get_balance(root.right) > 0:
        root.right = avl.right_rotate(root.right)
        return avl.left_rotate(root)
    return root

def traversal(root: Node, pre=None):
    s = []
    dic = []
    fit = []
    while root or s:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        if pre and len(pre)<=len(root.word) and checkPrefix(root.word,pre):
            fit.append(root.word)
        dic.append(root.word)
        root=root.right
    if pre:
        return fit
    return dic

def checkPrefix(w,pre):
    for i in range(len(pre)):
        if w[i] != pre[i]:
            return False
    return True

def search(root: Node, target: str):
    s = []
    while root or s:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        if (root.word==target):
            return root
        root=root.right
    return None

def complete(root: Node, pre: str):
    s = []
    result = []
    fit = False
    while root or s:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()

        root=root.right
    return dic

# start = Node("hi")
# start = insert(start,"apple")
# start = insert(start,"hailey")
# start = insert(start,"valerie")
# start = insert(start,"vscode")
# start = insert(start,"laptop")
# start = insert(start,"lap")
# start = insert(start,"app")
# start = insert(start,"zebra")

# print(traversal(start))
# print(start.word)