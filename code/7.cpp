/*
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

*/
#include<string>
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long reverse(int x) {
        bool flag=false;//是否为负数
        string str=to_string(x);
        long long result=0;

        int end=0;
        if(str[0]=='-'){
            flag=true;
            end=1;
        }

        for(int i=str.size()-1;i>=end;i--){
            result=result*10+(str[i]-'0');
        }
        
        if(flag){
            result=0-result;
        }
        if(result>2147483647 || result<=-2147483648){
            return 0;
        }
        return result;
    }
};