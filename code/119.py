# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 3
# 输出: [1,3,3,1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ress = []
        for i in range(rowIndex+1):
            res = []
            for j in range(0,i+1):
                if ((j == 0) | (j == i)):
                    res.append(1)
                else:
                    res.append(ress[i-1][j-1]+ress[i-1][j])
            ress.append(res)
        return ress[rowIndex]