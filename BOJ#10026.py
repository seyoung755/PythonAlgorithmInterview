N = int(input())
graph= []
rgraph = []

for i in range(N):
    a = list(input())
    graph.append(a[:])
    rgraph.append(a[:])

for i in range(N):

    for idx, color in enumerate(rgraph[i]):
        if color == 'G':
            rgraph[i][idx] = 'R'
    
# print(graph)
def BFS(graph):
    visited = [[False]*N for _ in range(N)]

    # print(visited)

    dir = [[-1,0],[0, 1], [1,0], [0,-1]]
    q = []
    RG = ['R', 'G']
    cnt = 0
    for x in range(N):
        for y in range(N):

            start = graph[x][y]
            if not visited[x][y]:
                q.append([x,y])
                visited[x][y] = start
                while q:
                    curx, cury = q.pop(0)
                    for dx, dy in dir:
                        nx, ny = curx+dx, cury+dy
                
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        if graph[nx][ny] == start and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = start
                            # print(visited)
                        
                        # elif start in RG and graph[nx][ny] in RG:
                        #     q.append([nx, ny])
                        #     visited[nx][ny] = start
                            
                            
                        
                cnt += 1
    return cnt
print(BFS(graph))
print(BFS(rgraph))