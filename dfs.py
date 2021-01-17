def recursive_dfs(start, discovered=[]):
    discovered.append(start)
    for v in graph[start]:
        if v not in discovered:
            discovered = recursive_dfs(v, discovered)
    return discovered




def stack_dfs(start, discovered=[]):
    
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


            
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

print(recursive_dfs(1))
print(stack_dfs(1))