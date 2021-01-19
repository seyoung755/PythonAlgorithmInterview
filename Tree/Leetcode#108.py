# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        # 배열의 가운데 (index가 배열 총 길이를 2로 나눈 몫) 요소를 기준으로
        # 좌 우로 쪼개고 쪼갠 배열에서 또 각각 가운데를 기준으로 나눠간다
        # 재귀로 구현
        
        def BinaryTree(nums, node = TreeNode()):
            
            
            if len(nums) == 1:
                node = TreeNode(nums[0])
                return node
            
            elif len(nums) == 0:
                return 
            
            n = len(nums) // 2
            
            
            node = TreeNode(nums[n])
            

            node.left = BinaryTree(nums[:n])
            
            if len(nums[n+1:]) != 0:
                node.right = BinaryTree(nums[n+1:])
                
            
            
            
            return node
        
        
       
        
        return BinaryTree(nums)