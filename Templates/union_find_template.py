
'''
The union find algorithm is like a game of blocks where you have a bunch of blocks, and you want to connect them together.
Each block has a number on it, and you can only connect blocks that have the same number. 
To connect two blocks, you draw a line between them.

The union find algorithm helps you keep track of which blocks are connected to each other. 
You can ask the algorithm if two blocks are connected, and it will tell you yes or no.
When you want to connect two blocks that have different numbers, 
you can join them together by changing the number on one of the blocks.
'''

def try_union_find(edges):
    n= len(edges)+1

    pars = [i for i in range(n)]  # setting each nodes parent as same

    def find(a):
        if pars[a]!=a:  # go till we found the root node
            pars[a]=find(pars[a]) # set parents of nodes as we traverse the connected graph
        return pars[a]

    def union(a,b):
        roota,rootb=find(a),find(b)
        if roota==rootb:  # indicates this edge is creating cycle
            return True
        pars[rootb]=roota # setting b's parent as a
        return False  # no cylce

    for a,b in edges:
        if union(a,b): return [a,b] 

    return [None,None] 

edges = [[1,2],[1,3],[2,3]]
try_union_find(edges)
