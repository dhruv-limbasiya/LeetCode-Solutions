class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n == 0:
            return True
            
        capital_count = 0
        for ch in word:
            if 65 <= ord(ch) <= 90:  
                capital_count += 1

        if capital_count == n:
            return True

        if capital_count == 0:
            return True

        if capital_count == 1 and 65 <= ord(word[0]) <= 90:
            return True

        return False