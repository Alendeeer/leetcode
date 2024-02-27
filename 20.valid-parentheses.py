#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return False
        
        tempRes = []
        count = 0
        for t in s:
            if t == "(":
                tempRes.append(1)
                count += 1
            elif t == ")":
                tempRes.append(-1)
                count -= 1
            elif t == "[":
                tempRes.append(2)
                count += 1
            elif t == "]":
                tempRes.append(-2)
                count -= 1
            elif t == "{":
                tempRes.append(3)
                count += 1
            else:
                tempRes.append(-3)
                count -= 1
        if count!=0 or sum(tempRes)!=0 or tempRes[0]<0:
            return False
        else:
            flag = 0
            for i in range(len(tempRes)):
                if tempRes[i] < 0:
                    if tempRes[i]+tempRes[i-(2*flag+1)] != 0 or (tempRes[i]+tempRes[len(tempRes)-i-1] != 0 and i < len(tempRes)-i-1):
                        return False
                    else:
                        flag += 1
                else:
                    flag = 0
            return True

        
# @lc code=end

print(Solution().isValid("([)]"))