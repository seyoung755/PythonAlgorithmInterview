# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        node = head
        while node.next:
        
            
            if node.val > node.next.val:
                node.val, node.next.val = node.next.val, node.val
                if node.next.next:
                    node.next, node.next.next = node.next.next, node
                else:
                    node.next.next, node.next = node, None
                    
        node = head.next
        print(head)