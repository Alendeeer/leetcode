#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            if m == 0:
                nums1 = []
            else: pass
        elif nums1 == [0]:
            nums1 = nums2
        else:
            temp = nums2[0]
            for i in range(len(nums1)-1):
                try:
                    nums1[i] = max(nums1[i], temp)
                    temp = min(nums1[i], temp)
                except IndexError:
                    
            
# @lc code=end
