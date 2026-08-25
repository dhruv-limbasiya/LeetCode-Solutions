class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        for i in range(1,200):
            temp = i * k
            if temp not in nums:
                return temp