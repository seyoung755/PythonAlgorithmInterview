class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 제일 많이 연결된 node가 (graph로 생각하면 edge가 많은 순) root여야 
        # min height tree가 가능
        if n <= 1:
            return [0]
        
        import collections
        
        graph = collections.defaultdict(list)
        
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
            
        leaves = []
        
        for i in range(n+1):
            
            if len(graph[i])== 1:
                leaves.append(i)
                
        # print(leaves)
        
        # root 후보는 최대 2개
        while n> 2:
            
            n -= len(leaves)
            new_leaves = []
            # edge가 하나인 node를 제거하고 1개가 된건 다시 leaf node로 추가
            for leaf in leaves:
            
                neighbor = graph[leaf].pop()
            
                graph[neighbor].remove(leaf)
            
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
        # 결국 마지막에 leaf node로 남은 node가 root node이므로 return
        
        # print(leaves)
        
        return leaves