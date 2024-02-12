#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        mid = len(xStr) // 2
        for i in range(mid):
            if xStr[i] != xStr[len(xStr)-i-1]:
                return False
            else:
                pass
        return True

# @lc code=end
