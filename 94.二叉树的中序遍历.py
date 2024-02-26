#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        if root.left:
            res = self.inorderTraversal(root.left)
            result.extend(res)
            return result
        elif root.right:
            res = self.inorderTraversal(root.right)
            return root.val
        else:
            try:
                result.append(root.val)
                return result
            except AttributeError:
                return []

        
# @lc code=end

a = [1, None, 2]
print(a)