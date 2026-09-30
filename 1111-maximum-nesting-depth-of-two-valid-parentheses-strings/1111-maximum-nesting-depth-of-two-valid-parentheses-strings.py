class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        c = 0
        
        for i in seq:
            if i == "(":
                ans.append(c % 2)
                c += 1 
            else:
                c -= 1
                ans.append(c % 2)

        return ans            