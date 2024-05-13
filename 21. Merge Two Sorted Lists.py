#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        handle = head #2nd pointer to handle List Node
        while list1 and list2:
            if list1.val < list2.val:
                handle.next = list1
                list1 = list1.next
            else:
                handle.next = list2
                list2 = list2.next
            handle = handle.next
        if list1:
            handle.next = list1
        elif list2:
            handle.next = list2
        return head.next

# @lc code=end

