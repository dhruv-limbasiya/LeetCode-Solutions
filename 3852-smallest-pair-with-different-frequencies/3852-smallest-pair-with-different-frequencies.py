class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = {}

        for i in nums:
            freq[i] = nums.count(i)

        values = sorted(freq.keys())

        for i in range(len(values)):
            for j in range(i+1, len(values)):
                x = values[i]
                y = values[j]

                if freq[x] != freq[y]:
                    return [x,y]

        return [-1,-1]            