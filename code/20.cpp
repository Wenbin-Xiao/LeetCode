/*

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

*/

#include<vector>
#include<string>
#include<stack>
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> sta1,sta2;
        int size=s.size();
        if(size==0){
            return true;
        }
        if(size%2!=0){
            return false;
        }
        for(int i=0;i<s.size();i++){
            if(s[i]=='('||s[i]=='{'||s[i]=='['){
                sta1.push(s[i]);
            }
            else{
                if(sta1.size()==0){
                    return false;
                }
                sta2.push(s[i]);
                char c1=sta1.top();
                sta1.pop();
                char c2=sta2.top();
                sta2.pop();
                if(c1=='('&&c2!=')'){
                    return false;
                }
                else if(c1=='{'&&c2!='}'){
                    return false;
                }
                else if(c1=='['&&c2!=']'){
                    return false;
                }
                else{

                    continue;
                }
            }
        }
        if(sta1.size()!=sta2.size()){
            return false;
        }
        // else{
        //     while(!sta1.empty()){
        //         char c1=sta1.top();
        //         sta1.pop();
        //         char c2=sta2.top();
        //         sta2.pop();
        //         if(c1=='('&&c2!=')'){
        //             return false;
        //         }
        //         else if(c1=='{'&&c2!='}'){
        //             return false;
        //         }
        //         else if(c1=='['&&c2!=']'){
        //             return false;
        //         }
        //         else{
        //             continue;
        //         }
        //     }
        // }
        return true;
    }
};