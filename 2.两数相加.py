#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        tempR = self.getNums(l1, 0) + self.getNums(l2, 0)
        tempR = str(tempR)
        result = [ListNode(int(tempR[0])), 0]
        for i in range(1, len(tempR)):
            if i % 2 == 1:
                result[1] = ListNode(int(tempR[i]), result[0])
            else:
                result[0] = ListNode(int(tempR[i]), result[1])
        result = result[(len(result)-1)%2]
        print([result])

    def getNums(self, listNode, times):
        if listNode.next:
            tempR = self.getNums(listNode.next, times+1)
            result = listNode.val*pow(10, times) + tempR
            return result
        else:
            result = listNode.val*pow(10, times)
            return result        

        
# @lc code=end
        