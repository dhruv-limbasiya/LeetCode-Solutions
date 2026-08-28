class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)

        ans = []

        for num in nums:
            if num not in ans:
                ans.append(num)

            if len(ans) == k:
                break

        return ans