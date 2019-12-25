class WeightedGraph:
    def __init__(self):
        self._raw_graph = {}

    def add(self, vertex):
        if not vertex in self._raw_graph.keys():
            self._raw_graph[vertex] = []
            return True
        
        return False

    def link(self, vertex_from, vertex_to, arch_weight):
        k = self._raw_graph.keys()

        if not vertex_from in k or not vertex_to in k:
            return False

        self._raw_graph[vertex_from].append((vertex_to, arch_weight))
        return True
        
    def unlink(self, vertex_from, vertex_to):
        k = self._raw_graph.keys()

        if not vertex_from in k or not vertex_to in k:
            return False

        for idx in range(len(self._raw_graph[vertex_from])):
            if self._raw_graph[vertex_from][idx][0] == vertex_to:
                del self._raw_graph[vertex_from][idx]
                return True

        return False

    def adj(self, vertex):
        return self._raw_graph[vertex]

def dfs(G, n, v = []):
    if not n in v:
        v.append(n)
        #print("just visited: {}".format(n))

        for nadj in G.adj(n):
            dfs(G, nadj[0], v)