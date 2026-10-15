class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        temp = 0

        for i in range(len(nums)):
            temp = temp + nums[i]
            ans.append(temp)

        return ans