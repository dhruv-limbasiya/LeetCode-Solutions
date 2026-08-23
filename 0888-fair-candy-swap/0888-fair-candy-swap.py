class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        SA = sum(aliceSizes) 
        SB = sum(bobSizes)

        target = (SA + SB) // 2 

        bob = set(bobSizes)
        for a in aliceSizes:
            b = target - SA + a

            if b in bob:
                return [a, b]

