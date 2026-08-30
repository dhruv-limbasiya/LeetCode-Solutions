class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        b = {}

        p = None

        for x in nums:
            if x != p:
                b[x] = b.get(x,0) +1
                p = x
        return sum(1 for x in b if b[x] == 1)    