class Node:
    def __init__(self,word: str):
        self.word = word 
        self.left = None
        self.right = None
        self.height = 1

def compare(w1: str, w2: str):
    for i in range(min(len(w1),len(w2))):
        if w1[i]<w2[i]:
            return -1
        if w1[i]>w2[i]:
            return 1
    if len(w1)<len(w2):
        return -1
    if len(w1)>len(w2):
        return 1
    else: return 0
    # -1: w1<w2   1: w1>w2  0:w1==w2