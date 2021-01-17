# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def height(node):
            
             # dfs로 leaf node부터 올라가면서 비교 -> height가 2 이상 차이나면 False 반환 
            
            if not node:
                # print("ok")
                return 0
            
            
        
            
            left = height(node.left) 
            right = height(node.right) 
            
            if abs(left-right) > 1 or \
                    right == -1 or \
                    left == -1:
                return -1
            
            return max(left, right) + 1
            
            
        
        return height(root) != -1
        
        