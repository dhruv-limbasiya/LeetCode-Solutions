class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                ans.append(s[i])
            else:
                if len(ans) == 0:
                    return False

                if (ans[-1] == "(" and s[i] == ")") or \
                   (ans[-1] == "{" and s[i] == "}") or \
                   (ans[-1] == "[" and s[i] == "]"):
                   ans.pop()
                else:
                    return False

        return len(ans) == 0                