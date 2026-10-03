class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = defaultdict(list)

        for i in strs:
            temp = "".join(sorted(i))
            freq[temp].append(i)

        return list(freq.values())         