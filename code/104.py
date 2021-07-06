# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root,max,res):
            if root == None:
                res.append(max)
                return
            max +=1
            max_1 = max
            max_2 = max
            dfs(root.left,max_1,res)
            dfs(root.right,max_2,res)
        res=[]
        max = 0
        dfs(root,max,res)
        max_res = -1
        for i in range(len(res)):
            if res[i]> max_res:
                max_res = res[i]
        return max_res
            