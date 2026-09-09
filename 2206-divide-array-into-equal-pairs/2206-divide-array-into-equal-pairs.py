class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for i in nums:
            freq[i] = nums.count(i)

        for i,j in freq.items():
            if j %2 != 0:
                return False

        return True            