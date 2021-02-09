# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def dfs(node, array = []):
            
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)
            
            array.append(node.val)
            return array
            
            
            
        nodes = dfs(root)
        print(nodes)
        
        dist = float('inf')
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                dist = min(dist, abs(nodes[i] - nodes[j]))
        return dist


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self. prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
            