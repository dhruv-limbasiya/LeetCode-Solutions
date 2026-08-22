class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            d = 0
            num = nums[i]
            while num != 0:
                num = num // 10
                d += 1

            if d%2 == 0:
                c+=1

        return c            