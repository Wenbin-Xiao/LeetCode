
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp = ""
        for i in range(len(s)):
            if s[i].isdigit() | s[i].isalpha():
                s_temp = s_temp + s[i]
        if s_temp == "":
            return True
        if s_temp[::1].upper() == s_temp[::-1].upper():
            return True
        return False