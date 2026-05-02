# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()
        # while head and head!=-1:
        #     if head in seen:
        #         return True
        #     else:
        #         seen.add(head)
        #         head = head.next
        # return False
        slow = fast = head
        while fast and fast.next and fast.next!=-1:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False        