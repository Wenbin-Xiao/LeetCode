# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


# Definition for a binary tree node.
# 思路没想到，暂时参考题解
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return (abs(self.treedept(root.left) - self.treedept(root.right)) <= 1) & self.isBalanced(root.left) & self.isBalanced(root.right)

    def treedept(self,root):
        if root == None:
            return 0
        return max(self.treedept(root.left),self.treedept(root.right)) + 1