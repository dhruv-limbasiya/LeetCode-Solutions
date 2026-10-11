class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)
        i = 0
        ans = []

        while i < n:
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{nums[i]}")

            i += 1

        return ans