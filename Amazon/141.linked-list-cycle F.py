#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# follow up: space complexty: O(1)

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            return self.judge(head, [])
        else:
            return False
    
    def judge(self, target: ListNode, flag: list) -> bool:
        if target.next:
            if target.next in flag:
                return True
            flag.append(target)
            return self.judge(target.next, flag)
        else:
            return False
        
# @lc code=end
