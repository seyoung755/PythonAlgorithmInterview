class Solution:
    def __init__(self):
        pass

    def nextGreaterElement(self, n: int) -> int:
        n_st = str(n)
        nums = list(n_st)[::-1]
        
        for i in range(len(nums)-1):

            
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
                return nextGreaterElement(int(''.join(e for e in nums[::-1])))

        
        return -1
            

            
        




answer = Solution()

print(answer.nextGreaterElement(1564))