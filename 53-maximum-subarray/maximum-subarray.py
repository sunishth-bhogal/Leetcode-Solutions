class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        best = nums[0]

        for num in nums:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            best = max(curr_sum, best)
            
        return best

                




