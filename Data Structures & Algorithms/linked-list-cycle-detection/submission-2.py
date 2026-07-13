# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hare = head
        turtle = head

        for _ in range(1000):
            if hare == None or hare.next == None:
                return False
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
            
        return False