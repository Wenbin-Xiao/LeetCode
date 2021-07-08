# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        first_list = []
        def dfs(root):
            if root == None:
                return
            first_list.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return first_list
             