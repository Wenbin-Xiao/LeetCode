# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos_1 = 0
        pos_2 = 0
        len_1 = m
        len_2 = n
        nums1_temp = nums1[0:m]
        nums2_temp = nums2[0:n]
        if len_1 == 0:
            nums1_temp = nums2_temp
        if len_2 == 0:
            nums1_temp = nums1_temp
        while True:
            if ((len_1!=0) & (len_2 != 0) & (pos_1 < len_1) & (pos_2 < len_2)):
                if nums1_temp[pos_1] > nums2_temp[pos_2]:
                    nums1_temp.insert(pos_1,nums2_temp[pos_2])
                    pos_2 = pos_2 + 1
                    pos_1 = pos_1 + 1
                    len_1 = len(nums1_temp)
                else:
                    pos_1 = pos_1 + 1
            else:
                break
        if pos_2 < len_2:
            for i in range(pos_2,len_2):
                nums1_temp.append(nums2_temp[i])
        for i in range(m+n):
            nums1[i] = nums1_temp[i]
            

            
