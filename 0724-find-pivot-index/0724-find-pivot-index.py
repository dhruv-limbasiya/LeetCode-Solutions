class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = right_sum - nums[i] 

            if left_sum == right_sum:
                return i

            left_sum = left_sum + nums[i]

        return -1        