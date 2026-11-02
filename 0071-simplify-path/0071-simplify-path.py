class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []

        for i in arr:
            if i == ".." and stack:
                stack.pop()
            elif i != "" and i != "." and i != "..":
                stack.append(i)

        ans = ""

        for i in stack:
            ans += "/" + i
        
        return ans if ans else "/"