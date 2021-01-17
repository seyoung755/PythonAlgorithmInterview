import collections

N, M, start = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    


def dfs(v, visited=[]):
    visited.append(v)
    for w in sorted(graph[v]):
        if not w in visited:
            visited = dfs(w, visited)
    return visited

print(*dfs(start))

discovered = []
stack = [start]

while stack:
    v = stack.pop(0)
    if v not in discovered:
        discovered.append(v)
        for w in sorted(graph[v]):
            stack.append(w)
print(*discovered)


# dic = {1: [6,2,3,4]}
# print(sorted(dic[1]))