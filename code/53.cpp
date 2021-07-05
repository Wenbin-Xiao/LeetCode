/*
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
201/203未通过，超时
*/
#include<vector>
#include<string>
#include<set>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = -99999999;
        //第一个for寻找位数，1——length
        for(int i = 1; i <= nums.size(); i++){
            for(int j = 0;j<nums.size();j++){
                long long temp = 0;
                int flag = 0;
                for(int k = 0 ;k < i; k++){  
                    int pos = j+k;
                    if(pos>=nums.size()){
                        flag = 1;
                        break;
                    }
                    temp = temp + nums[pos];
                }
                if(max < temp){
                    max = temp;
                }
                if(flag == 1){
                    break;
                }
            }

        }
        return max;
    }
};