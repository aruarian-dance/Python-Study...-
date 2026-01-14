class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def set_next(self, node):
        self.next = node
    def __repr__(self):
        return self.val
    
class linked_list:
    pass

class undirected_graph():
    def __init__(self, V: list, E: list) -> None:
        self.V = V[:]
        self.neighbor = {}
        for v in V:
            self.neighbor[v] = []
        for (v, w) in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)
    
    def depth_first_traversal(self) -> None:
        if self.V:
            visited = {}
            for v in self.V:
                visited[v] = False
            for v in self.V:
                self.DFTHelp(visited, v)
    
    def DFTHelp(self, visited: list, v: int) -> None:
        if not visited[v]:
            visited[v] = True
            print(v)
            for w in self.neighbor[v]:
                self.DFTHelp(visited, w)