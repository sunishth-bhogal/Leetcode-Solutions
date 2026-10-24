class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = sorted(nums1 + nums2)
        len_of_array = len(combined)

        if len_of_array % 2 == 0:
            mid1 = combined[(len_of_array//2) - 1]
            mid2 = combined[(len_of_array//2)]
            median = (mid1 + mid2)/2
        else: 
            median = combined[(len_of_array//2)]
        
        return median
        