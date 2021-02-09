M, N = map(int, input().split())

graph = []
for i in range(M):
    row = list(map(int, input().split()))
    graph.append(row)

maxlen = -float('inf')

# print(graph)   
dir = [[-1,0], [0, 1], [1, 0], [0, -1]]
result = []
visited = [[False]*N for _ in range(M)]

for x in range(M):
    for y in range(N):
        start = [x,y]
        if graph[x][y] == 0 or visited[x][y]:
            continue

        
        # print(start)
        

        queue = [start]    
        visited[x][y] = True
        result.append([start])
        area = 1
        while queue:
            cur_x, cur_y = queue.pop()
    
            for dx, dy in dir:
                nx, ny = cur_x+dx, cur_y+dy
                if 0 <= nx < M and 0 <= ny < N:
                    # if graph[nx][ny] == 1 and [nx, ny] not in visited:
                    if graph[nx][ny] and not visited[nx][ny]:
                        queue.append([nx, ny])
                        # visited.append([nx, ny])
                        visited[nx][ny] = True
                        result[-1].append([nx, ny])
                        area += 1
        
        maxlen = max(maxlen, area)


print(len(result) if result else 0)
print(maxlen if result else 0)

# print(visited)
# print(result)
        
