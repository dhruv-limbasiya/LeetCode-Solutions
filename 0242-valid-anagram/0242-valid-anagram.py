class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        f1 = {}

        for i in s:
            f1[i] = s.count(i)

        f2 = {}

        for i in t:
            f2[i] = t.count(i)

        return f1 == f2    