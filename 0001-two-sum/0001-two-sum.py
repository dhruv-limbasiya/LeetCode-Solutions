class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}

        for i in range(len(nums)):
            want = target - nums[i]

            if want in d:
                return [d[want], i]

            d[nums[i]] = i    

        return ans        