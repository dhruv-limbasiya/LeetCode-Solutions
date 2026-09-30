class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}

        for i in strs:
            k = "".join(sorted(i))

            if k not in ans:
                ans[k] = []

            ans[k].append(i)

        return list(ans.values())        