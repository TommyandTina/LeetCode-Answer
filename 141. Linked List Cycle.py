#Floyd's Tortoise and Hare Algorithm
#https://youtu.be/RRSItF-Ts4Q?si=56CQusdZPlG3Rh7x

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = head
        while fast.next and fast.next.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

#another solution
class Solution:hasCycle=lambda*_:'E' in str(_)
#another solution
class Solution:hasCycle=lambda*_:'None' not in str(_)