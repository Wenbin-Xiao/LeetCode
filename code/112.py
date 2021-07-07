# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

# 叶子节点 是指没有子节点的节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        if (root.left==None) & (root.right == None):
            return targetSum == root.val
        return self.hasPathSum(root.left,targetSum-root.val) | self.hasPathSum(root.right,targetSum-root.val)