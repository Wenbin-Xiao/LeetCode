# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明：叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if (root.left == None) & (root.right != None):
            return 1+rightDepth
        if (root.left !=None) & (root.right == None):
            return 1+leftDepth
        return min(leftDepth,rightDepth)+1