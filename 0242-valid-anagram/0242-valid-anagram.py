class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        f1 = defaultdict(int)

        for i in s:
            f1[i] += 1

        f2 = defaultdict(int)

        for i in t:
            f2[i] += 1

        return f1 == f2    