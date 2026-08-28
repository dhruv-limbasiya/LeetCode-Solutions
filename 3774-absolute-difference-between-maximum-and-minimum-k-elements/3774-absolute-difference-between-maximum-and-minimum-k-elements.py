class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        first_two = 0
        last_two = 0

        for i in range(k):
            first_two += nums[i]

        for j in range(len(nums)-k, len(nums)):
            last_two += nums[j]

        return abs(first_two - last_two)        