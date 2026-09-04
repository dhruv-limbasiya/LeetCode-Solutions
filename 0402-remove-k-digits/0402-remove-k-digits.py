class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []

        for d in num:
            while s and k > 0 and s[-1] > d:
                s.pop()
                k -= 1

            s.append(d)

        while k > 0:
            s.pop()
            k -= 1

        r = ''.join(s).lstrip('0')

        return r if r else "0"