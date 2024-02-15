#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # v1, using index()
        if haystack is None:
            return -1
        elif needle in haystack:
            ind = haystack.index(needle)
            return ind
        else:
            return -1
# @lc code=end
