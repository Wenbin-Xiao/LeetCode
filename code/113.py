# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root,targetSum):
            if root == None:
                return
            res.append(root.val)
            if (root.left==None) & (root.right==None):
                if root.val == targetSum:
                    ress.append(res[:])
            targetSum = targetSum - root.val
            dfs(root.left,targetSum)
            dfs(root.right,targetSum)
            res.pop()
        ress = []
        res = []
        dfs(root,targetSum)
        return ress