# Traverse a tree using depth first search 

class Node:
    def __init__(self, name): 
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self 

    def depthFirstSearch(self, array):
        # call the first node: A
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array 



