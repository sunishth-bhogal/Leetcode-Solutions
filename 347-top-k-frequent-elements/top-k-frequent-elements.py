class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
        pairs = list(count.items())
        pairs.sort(key=lambda x: x[1], reverse= True)
        top_k = pairs [: k]

        result = [pair[0] for pair in top_k]
        return result
