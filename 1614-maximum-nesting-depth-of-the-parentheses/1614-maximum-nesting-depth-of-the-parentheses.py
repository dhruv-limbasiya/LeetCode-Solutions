class Solution:
    def maxDepth(self, s: str) -> int:
        temp = 0
        maxi = 0

        for i in range(len(s)):
            if s[i] == "(":
                temp += 1
                maxi = max(temp,maxi)
            elif s[i] == ")":
                temp -= 1

        return maxi            
        
