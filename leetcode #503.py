class Solution:
    def __init__(self):
        pass

    def nextGreaterElements(self, nums):
        if not nums:
            return []

        num_ = nums + nums
        stack = []
        answer = [None] * len(num_)

        

        for i, num in enumerate(num_):
            
            
            while stack and num>num_[stack[-1]]:                                                                                                                                                                                                                                                               
                answer[stack.pop()] = num


            stack.append(i)
        
        return [-1 if n is None else n for n in answer[:len(nums)]]

answer = Solution()

print(answer.nextGreaterElements([1,2,1]))