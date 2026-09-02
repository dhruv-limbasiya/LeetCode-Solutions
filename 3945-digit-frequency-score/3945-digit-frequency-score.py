from collections import defaultdict
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        
        freq = defaultdict(int)

        for i in s:
            freq[i] += 1

        ans = 0

        for i,j in freq.items():
            ans += int(i) * j
            
        return ans
