# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_num1 = len(a)-1
        len_num2 = len(b)-1
        d_num1 = 0
        d_num2 = 0
        for i in a:
            if i == '1':
                int_temp = pow(2,len_num1)
                d_num1 = d_num1 + int_temp
                len_num1 = len_num1 - 1
            else:
                len_num1 = len_num1 - 1

        for i in b:
            if i == '1':
                int_temp = pow(2,len_num2)
                d_num2 = d_num2 + int_temp
                len_num2 = len_num2 - 1
            else:
                len_num2 = len_num2 - 1
        int_res = d_num1 + d_num2
        bin_res = bin(int_res)
        str_res = str(bin_res)[2:]
        return str_res
