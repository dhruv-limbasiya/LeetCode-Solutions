class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for i in s:
            if i in "aeiouAEIOU":
                v.append(i)

        result = ""
        for i in s:
            if i in "aeiouAEIOU":
                result = result + v.pop()
            else:
                result = result + i
                
        return result                    