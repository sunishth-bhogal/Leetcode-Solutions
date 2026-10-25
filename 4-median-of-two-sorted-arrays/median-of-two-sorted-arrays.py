class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1

        combined += nums1[i:]
        combined += nums2[j:]

        len_of_array = len(combined)

        if len_of_array % 2 == 0:
            mid1 = combined[(len_of_array//2) - 1]
            mid2 = combined[(len_of_array//2)]
            median = (mid1 + mid2)/2
        else: 
            median = combined[(len_of_array//2)]
        
        return median
        