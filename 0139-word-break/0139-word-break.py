class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)

        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        n = len(s) 

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i-1, max(0,i-maxLen) - 1, -1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n] 