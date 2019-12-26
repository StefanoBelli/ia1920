import heapq

INFTY = float('inf')

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
        
    def link_weight(self, vertex_from, vertex_to):
        k = self._raw_graph.keys()

        if not vertex_from in k or not vertex_to in k:
            return False

        for links in self._raw_graph[vertex_from]:
            if links[0] == vertex_to:
                return links[1]

        return False

    def vertices(self):
        return [ key for key,_ in self._raw_graph.items() ]

def dfs(G, n, v = []):
    if not n in v:
        v.append(n)
        #print("just visited: {}".format(n))

        for nadj in G.adj(n):
            dfs(G, nadj[0], v)

def priority_queue_find(q, e):
    for key, value, prev in q:
        if e == value:
            return (key, prev)

    return False

def priority_queue_replace(q, e, r, p):
    q.remove(e)
    heapq.heappush(q, (r, e[1], p))

def dijkstra(G, s):
    ret = {}
    pq = []

    for vertex in G.vertices():
        if vertex == s:
            heapq.heappush(pq, (0, vertex, None))
        else:
            heapq.heappush(pq, (INFTY, vertex, None))

    while len(pq) > 0:
        vertex = heapq.heappop(pq)

        for adj_vertex in G.adj(vertex[1]):
            cur_vertex_total = priority_queue_find(pq, adj_vertex[0])
            new_dist = vertex[0] + G.link_weight(vertex[1], adj_vertex[0]) 

            if cur_vertex_total:
                prev = cur_vertex_total[1]
                cur_vertex_total = cur_vertex_total[0]
            
                if new_dist < cur_vertex_total:
                    priority_queue_replace(pq, (cur_vertex_total, adj_vertex[0], prev), new_dist, vertex[1])
                    ret[adj_vertex[0]] = (new_dist, vertex[1])

    return ret
