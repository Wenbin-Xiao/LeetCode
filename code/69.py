# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 二分法
# 精度问题，二分法无法解决
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        min_num = 0.0
        max_num = float(x)
        mid_num = (min_num + max_num) / 2
        print(mid_num)
        EPSIONN = 0.000001
        while (max_num - min_num) > EPSIONN:
            if (mid_num * mid_num) > float(x):
                max_num = mid_num
            else:
                min_num = mid_num
            mid_num = (max_num + min_num) / 2
            print(mid_num)
        int_num = int(mid_num)
        if abs(float(int_num-mid_num)) >=0.99:
            int_num = int_num + 1
        return int_num
