# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import builtins


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ress = []
        for i in range(numRows):
            res = []
            for j in range(0,i+1):
                if ((j == 0) | (j == i)):
                    res.append(1)
                else:
                    res.append(ress[i-1][j-1]+ress[i-1][j])
            ress.append(res)
        return ress
        
