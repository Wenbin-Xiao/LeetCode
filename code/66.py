
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""
        for i in range(len(digits)):
            str_num = str_num + str(digits[i])
        int_num = int(str_num)
        int_num = int_num + 1
        str_num = str(int_num)
        for i in range(len(str_num)):
            if(i >= len(digits)):
                digits.append(0)
            else:
                digits[i] = int(str_num[i])
        return digits



