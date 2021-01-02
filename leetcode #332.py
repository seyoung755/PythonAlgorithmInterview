class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import collections
        graph = collections.defaultdict(list)
        
        
        for a,b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            print(route)
            
        print(graph)
        dfs('JFK')
        return route[::-1]