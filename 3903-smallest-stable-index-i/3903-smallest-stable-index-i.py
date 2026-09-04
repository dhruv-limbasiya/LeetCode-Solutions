class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi = nums[0]

        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            mini = nums[i]
            
            for j in range(i, len(nums)):
                mini = min(mini, nums[j])

            ans = maxi - mini

            if ans <= k:
                return i

        return -1           
