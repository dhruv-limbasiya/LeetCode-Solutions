class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for i in set(nums):
            freq[i] = nums.count(i)

        for i, j in freq.items():
            if j == 1:
                return i