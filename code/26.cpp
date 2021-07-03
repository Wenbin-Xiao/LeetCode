/*

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
*/
#include<vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int list_len = nums.size();
        int begin_pos = 0,count=1;
        if(list_len==0){
            return 0;
        }
        for(int i=1;i<list_len;i++){
            if(nums[begin_pos]!=nums[i]){
                count++;
                begin_pos++;
                nums[begin_pos] = nums[i];
            }
            else{

            }
        }
        return count;
    }
};