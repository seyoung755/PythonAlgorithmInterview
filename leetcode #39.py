class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        import copy
        
        def dfs(start, index):
            if sum(start) > target:
                return
            
            if sum(start) == target:
                results.append(copy.deepcopy(start))
                return
            
            for i in range(index, len(candidates)):
                start.append(candidates[i])
                print(start, sum(start))
                dfs(start, i)
                start.pop()
                
                    
                    
            
        
        dfs([], 0)
        return results