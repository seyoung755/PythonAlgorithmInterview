class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq

lists = [[1,4,5], [1,3,4], [2,6]]
heap = []


for i in range(len(lists)):
    heapq.heappush(heap, (lists[i].val, i, lists[i]))
