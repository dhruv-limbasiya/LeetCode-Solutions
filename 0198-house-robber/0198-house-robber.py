class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0

        for i in nums:
            curr = max(a+i, b)
            a = b
            b = curr

        return b    