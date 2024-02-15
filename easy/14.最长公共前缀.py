#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        temp = []
        output = ""
        for _ in range(self.getMax(strs)):
            temp.append([])
        for s in strs:
            if s == "":
                return output
            else:
                for j in range(len(s)):
                    try:
                        temp[j].append(s[j])
                    except IndexError:
                        temp[j].append("")
        try:
            while len(temp[i]) == len(strs) and len(set(temp[i])) == 1:
                output += str(temp[i][0])
                i += 1
        except IndexError:
            pass
        print(output)
        return output

    def getMax(self, target):
        length = []
        for s in target:
            length.append(len(s))
        return max(length)
# @lc code=end

