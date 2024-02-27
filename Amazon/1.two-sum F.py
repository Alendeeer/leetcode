#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# Follow up: time complexity < O(n^2)

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            try:
                if i != nums.index(target-nums[i]):
                    return [i, nums.index(target-nums[i])]
            except ValueError:
                nums.pop()
        return []

        
# @lc code=end

