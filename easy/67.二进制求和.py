#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # v1 by me, traditional way
        # if a == "0":
        #     return b
        # elif b =="0":
        #     return a
        # else:
        #     resi = ""
        #     pre = 0
        #     res = list(str(int(a)+int(b)))
        #     for i in range(len(res)-1, -1, -1):
        #         temp = int(res[i])+pre
        #         if i != 0:
        #             if temp == 2:
        #                 res[i] = "0"
        #                 pre = 1
        #             elif temp == 3:
        #                 res[i] = "1"
        #                 pre = 1
        #             else:
        #                 res[i] = str(temp)
        #                 pre = 0
        #         else:
        #             if temp < 2:
        #                 return res[i] + resi
        #             elif temp == 2:
        #                 res[i] = "0"
        #             elif temp == 3:
        #                 res[i] = "1"
        #             else:
        #                 pass
        #             resi = res[i] + resi
        #             resi = "1" + resi
        #             return resi
        #         resi = res[i] + resi
        #     return resi

        # v2 by me, using bin() type (reminded by GPT)
        result = bin(int("0b"+a, 2)+int("0b"+b, 2))
        return result[2:]

# @lc code=end