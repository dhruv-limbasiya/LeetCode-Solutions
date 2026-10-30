class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = nums.count(i)

        
        for i, j in freq.items():
            if j == 1:
                return i