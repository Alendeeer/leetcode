#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # v1 by me, use list
        if digits[0] == 0:
            return [1]
        elif digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1
        else:
            digits[len(digits)-1] += 1
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 10 and i != 0:
                    digits[i] = 0
                    digits[i-1] += 1
                elif digits[i] == 10 and i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                else:
                    break
        return digits

        # v2 by me, try to use deque while the speed doesn't improve
        # import collections
        # digits = collections.deque(digits)
        # if digits[0] == 0:
        #     return [1]
        # elif digits[len(digits)-1] != 9:
        #     digits[len(digits)-1] += 1
        # else:
        #     digits[len(digits)-1] += 1
        #     for i in range(len(digits)-1, -1, -1):
        #         if digits[i] == 10 and i != 0:
        #             digits[i] = 0
        #             digits[i-1] += 1
        #         elif digits[i] == 10 and i == 0:
        #             digits[i] = 0
        #             digits.appendleft(1)
        #         else:
        #             break
        # return list(digits)
# @lc code=end
