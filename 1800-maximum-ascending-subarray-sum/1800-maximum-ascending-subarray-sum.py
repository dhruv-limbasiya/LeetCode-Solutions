class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        maxi = nums[0]

        for i in range(1,len(nums)):
            temp = 0
            if nums[i] > nums[i-1]:
                maxi += nums[i]
            else:
                maxi = nums[i]   

            ans = max(ans, maxi)     
            
        return ans