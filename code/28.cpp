/*
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
#include<vector>
#include<string>
#include<set>
using namespace std;
class Solution {
public:
    int strStr(string haystack, string needle) {
        set<char> s1,s2;
        int len_str_1 = haystack.size();
        int len_str_2 = needle.size();
        bool flag=false;
        int pos = -1;
        // 测试有时间限制，需要判断set的大小
        for(int i = 0;i<len_str_1;i++){
            s1.insert(haystack[i]);
        }
        for(int i = 0;i<len_str_2;i++){
            s2.insert(needle[i]);
        }
        if(len_str_2 ==0){
            return 0;
        }
        else if((len_str_1 < len_str_2)||(s1.size()<s2.size())){
            return -1;
        }
        else{
            for(int i = 0;i<len_str_1;i++){
                int temp = i;
                int count = 0;
                for(int j = 0;j<len_str_2;j++){
                    if(haystack[temp]==needle[j]){
                        temp++;
                        count++;
                    }
                    if(count == len_str_2){
                        flag = true;
                    }
                }
                if(flag == true ){
                    pos = i;
                    break;
                }
            }
        }
        return pos;
    }
};