#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        flag = 0
        for n in nums:
            temp = target - n
            if temp in nums[flag+1:]:
                nums.pop(flag)
                iTemp = nums.index(temp)
                return [flag, iTemp+1]
            else:
                pass
            flag += 1

# @lc code=end

