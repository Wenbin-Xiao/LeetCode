# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [3,2,1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        end_list = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            end_list.append(root.val)
        dfs(root)
        return end_list