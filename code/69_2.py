
# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 牛顿迭代法
class Solution:
    def mySqrt(self, x: int) -> int:
        EPSIONN = 0.1
        int_temp = x
        if x == 0:
            return 0
        while abs(int_temp * int_temp - x) > EPSIONN:
            int_temp = (int_temp + x / int_temp) / 2
        int_temp = int(int_temp)
        return int_temp

