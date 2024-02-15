#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # O(n) by GPT
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
        # O(n^2) by me
        # i = 0
        # while True:
        #     try:
        #         if nums[i] == nums[i+1]:
        #             nums.pop(nums.index(nums[i]))
        #         else:
        #             i += 1
        #     except IndexError:
        #         break  
        # return len(nums)
# @lc code=end
sss = Solution()
sss.removeDuplicates([1,1,2])
  