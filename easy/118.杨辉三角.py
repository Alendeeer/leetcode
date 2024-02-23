#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pre = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return pre
        else:
            for i in range(2, numRows):
                temp = []
                for j in range(i):
                    if j == 0:
                        temp.append(1)
                    else:
                        temp.append(pre[i-1][j-1]+pre[i-1][j])
                temp.append(1)
                pre.append(temp)
            return pre

# @lc code=end

