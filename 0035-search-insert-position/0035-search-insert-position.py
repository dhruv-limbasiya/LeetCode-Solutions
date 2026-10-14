class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        for i in range(len(nums)):
            if nums[i] > target:
                return i

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < target:
                return i + 1        