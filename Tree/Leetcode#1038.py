# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:

        if root:
            self.bstToGst(root.right)
            self.val += root.val # 맨 오른쪽 노드의 값부터 시작해서 차례로 더해짐
            root.val = self.val # 조회한 노드의 값 업데이트(맨 오른쪽의 경우 자기자신과 동일, 그 다음부터 차례로 큰 노드의 값이 더해짐) 
            self.bstToGst(root.left) # 부모 노드의 오른쪽 자식 -> 부모 노드 -> left 순으로 하여 , left는 부모의 값 + 오른쪽 값이 모두 더해지도록 만듬
            
        return root