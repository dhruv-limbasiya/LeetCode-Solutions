class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        c = 0
        for i in range(k):
            c += nums[i]
        
        maxi = c
        for i in range(1, len(nums)-k+1):
            c = c - nums[i-1] + nums[i+k-1]

            if c > maxi:
                maxi = c

        return maxi / k