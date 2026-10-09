class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        s2 = ""

        for i in range(len(temp) - 1, -1, -1):
            s2 += temp[i] + " "

        return s2.strip()
