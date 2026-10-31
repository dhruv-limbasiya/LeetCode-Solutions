class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for i in strs:
            temp = "".join(sorted(i))
            ans[temp].append(i)
        
        return list(ans.values())