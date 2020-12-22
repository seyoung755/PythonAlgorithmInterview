from collections import deque

def bfs(num):
    
    start = 0
    end = len(num)-1
    
    visited = [False] * len(num)
    count = 0
    queue = deque([[start, count]])
    visited[start] = True
    
    

    while queue:

        v = queue.popleft()
        cnt = v[1]
        print(v)
        # cnt = queue.pop(0)
        
        if v[0] == end:
            return cnt

        next = v[0] + num[v[0]]
        prev = v[0] - num[v[0]]
        
        if next <= len(num):
            if not visited[next]:
                visited[next] = True
                queue.append([next, cnt+1])
                
        
        if prev >= 0:
            if not visited[prev]:
                visited[prev] = True
                queue.append([prev, cnt+1])
        
        
        
        
    return -1
        

bfs([4,1,2,3,2,0,5])