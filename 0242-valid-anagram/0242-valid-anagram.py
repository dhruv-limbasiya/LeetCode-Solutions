class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ss = defaultdict(int)
        tt = defaultdict(int)

        for i in s:
            ss[i]+=1

        for i in t:
            tt[i]+=1

        return ss == tt    


