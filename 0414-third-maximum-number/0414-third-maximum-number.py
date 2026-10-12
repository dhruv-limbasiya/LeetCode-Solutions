class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        ans = sorted(set(nums), reverse=True)

        if len(ans) >= 3:
            return ans[2]
        else:
            return ans[0]    