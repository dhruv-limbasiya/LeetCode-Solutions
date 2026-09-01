class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        ans = []
        ans2 = []

        for i in s:
            if i == "#":
                if ans:
                    ans.pop()
            else:
                ans.append(i)

        for i in t:
            if i == "#":
                if ans2:
                    ans2.pop()
            else:
                ans2.append(i)

        return ans == ans2            
