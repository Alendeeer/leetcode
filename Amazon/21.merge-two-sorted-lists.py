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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            result = ListNode()
            if list1.val < list2.val:
                result.val = list1.val
                result.next = self.mergeTwoLists(list1.next, list2)
            else:
                result.val = list2.val
                result.next = self.mergeTwoLists(list1, list2.next)
            return result

        
# @lc code=end

