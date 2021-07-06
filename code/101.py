# 给定一个二叉树，检查它是否是镜像对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs_left(tree,res):
            if tree == None:
                res.append(-999999)
                return
            res.append(tree.val)
            dfs_left(tree.left,res)
            dfs_left(tree.right,res)
        def dfs_right(tree,res):
            if tree == None:
                res.append(-999999)
                return
            res.append(tree.val)
            dfs_right(tree.right,res)
            dfs_right(tree.left,res)
        res1=[]
        res2=[]
        dfs_left(root.left,res1)
        dfs_right(root.right,res2)
        if res1==res2:
            return True
        else:
            return False