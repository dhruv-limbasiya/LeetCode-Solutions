class Solution:
    def removeOuterParentheses(self, s):
        ans = []
        d = 0

        for ch in s:

            if ch == '(':
                if d > 0:
                    ans.append(ch)

                d += 1

            else:
                d -= 1

                if d > 0:
                    ans.append(ch)

        return ''.join(ans)
