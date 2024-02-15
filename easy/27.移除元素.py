#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # O(n^2)? by me, Ver.1
        # i = 0
        # while True:
        #     try:
        #         if nums[i] == val:
        #             nums.pop(i)
        #         else:
        #             i += 1
        #     except IndexError:
        #         break
        # return i

        # O(n)? by me, Ver.2
        if nums is None:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == val:
                pass
            else:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i
                
# @lc code=end
