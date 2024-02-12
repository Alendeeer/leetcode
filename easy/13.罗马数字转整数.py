#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        intStr = []
        result, i = 0, 0
        s = list(s)
        for ele in s:
            intStr.append(self.checkNumOrder(ele))
        while i < len(intStr)-1:
            if intStr[i] < intStr[i+1]:
                intStr[i+1] -= intStr[i]
                intStr.pop(i)
            else: 
                pass
            result += intStr[i]
            i += 1
        if i != len(intStr):
            result += intStr[len(intStr)-1]
        return result

    def checkNumOrder(self, word: str):
        if word == 'M':
            return 1000
        elif word == 'D':
            return 500
        elif word == 'C':
            return 100
        elif word == 'L':
            return 50
        elif word == 'X':
            return 10
        elif word == 'V':
            return 5
        else:
            return 1

# @lc code=end
