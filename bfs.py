import collections
def bfs(start, discovered=[]):
    q = collections.deque([start])
    while q:
        v = q.popleft()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                q.append(w)
    return discovered


import copy

            
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

g = copy.deepcopy(graph)
print(g)
print(bfs(1))