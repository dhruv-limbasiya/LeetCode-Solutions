class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""

        for i in digits:
            s += str(i)

        a = str(int(s) + 1)
        
        ans = []

        for i in a:
            ans.append(int(i))

        return ans       