class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        median = 0

        if n%2 == 1:
            median = nums[n//2]
        else:
            median = (nums[n//2] + nums[n//2]) // 2
        
        ans = 0
        for i in nums:
            ans += abs(i - median)
        
        return ans