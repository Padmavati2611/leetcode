
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        count = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        dummy = ListNode()
        current = dummy

        while heap:
            val, _, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                count += 1
                heapq.heappush(heap, (node.next.val, count, node.next))

        return dummy.next
