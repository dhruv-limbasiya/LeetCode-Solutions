class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()

        ans = ""

        first_word = list(strs[0])
        last_word = list(strs[len(strs)-1])
        
        for i in range(len(first_word)):
            if first_word[i] == last_word[i]:
                ans += first_word[i]
            else:
                break    

        return ans        