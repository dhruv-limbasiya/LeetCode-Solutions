class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)

        mn = mn + k
        mx = mx - k

        return max(0, mx - mn)