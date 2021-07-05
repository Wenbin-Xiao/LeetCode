/*
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
#include<vector>
#include<string>
#include<set>
class Solution {
public:
    int lengthOfLastWord(string s) {
        int length_word = 0;
        int s_size = s.size();
        if(s.size()==0){
            return length_word;
        }
        else{
            for(int i = s.size()-1;i>=0;i--){
                if(s[i]!=' '){
                    break;
                }
                else{
                    s_size--;
                }
            }
            for(int j = s_size-1;j>=0;j--){
                if(s[j]!=' '){
                    length_word++;
                }
                else{
                    return length_word;
                }
            }
        }
        return length_word;
    }
};