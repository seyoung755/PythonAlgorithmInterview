class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import copy
        results = []
        
        def dfs(elements, index):
            
            results.append(copy.deepcopy(elements))
        
            # if len(elements) <= len(nums):
            for i in range(index, len(nums)):
                elements.append(nums[i])
                print(elements)
                dfs(elements, i+1)
                elements.pop()
            
            return
                    
        dfs([], 0)
        return results