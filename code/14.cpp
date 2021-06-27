/*

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

*/

#include<vector>
#include<string>
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string yes="";
        int pos=0;
        if(strs.empty()){
            return yes;
        }
        int size=strs.size();
        if(size==1){
            yes=strs[0];
            return yes;
        }
        int minsize=99999;
        for(int i=0;i<size;i++){
            if(minsize>strs[i].size()){
                minsize=strs[i].size();
            }
            if(strs[i]==""){
                return yes;
            }
        }
        bool end=false;
        while(true){
            for(int i=0;i<size-1;i++){
                if(strs[i][pos]!=strs[i+1][pos]){
                    end=true;
                }
            }
            if(!end){
                pos++;
                if(pos==minsize){
                    break;
                }
            }
            else{
                break;
            }
        }
        for(int i=0;i<pos;i++){
            yes=yes+strs[0][i];
        }
        return yes;
    }
};