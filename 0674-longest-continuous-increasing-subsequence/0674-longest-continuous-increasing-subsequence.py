class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c = 1
        max_c = 0

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                c += 1
            else:
                max_c = max(max_c, c)
                c = 1

        return max(max_c,c)          