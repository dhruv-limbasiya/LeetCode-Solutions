class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        ans = []

        for i in nums:
            right_sum = total - left_sum - i
            ans.append(abs(left_sum - right_sum))

            left_sum += i

        return ans    