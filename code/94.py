
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(tree,res):
            if tree == None:
                return
            dfs(tree.left,res)
            res.append(tree.val)
            dfs(tree.right,res)
        res = []
        dfs(root,res)
        return res