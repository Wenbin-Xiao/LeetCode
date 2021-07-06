# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(tree,res):
            if tree == None:
                res.append(-999999)
                return
            res.append(tree.val)
            dfs(tree.left,res)
            dfs(tree.right,res)
        res1=[]
        res2=[]
        dfs(p,res1)
        dfs(q,res2)
        if res1==res2:
            return True
        else:
            return False
        # return flag

