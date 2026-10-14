class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        ans = ""

        for i in range(len(temp)-1, -1, -1):
            ans += temp[i] + " "

        return ans.strip()