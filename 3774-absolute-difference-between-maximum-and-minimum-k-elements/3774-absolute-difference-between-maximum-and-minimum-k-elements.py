class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        a = 0
        b = 0
        for i in range(k):
            a+=nums[i]

        for i in range(len(nums)-k, len(nums)):
            b+=nums[i]    
            
        return abs(a-b)