from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        ans = []
        
        for word in words:
            lower_word = word.lower()
            
            in_row1 = True
            for char in lower_word:
                if char not in row1:
                    in_row1 = False
                    break
            
            in_row2 = True
            for char in lower_word:
                if char not in row2:
                    in_row2 = False
                    break
            
            in_row3 = True
            for char in lower_word:
                if char not in row3:
                    in_row3 = False
                    break

            if in_row1 or in_row2 or in_row3:
                ans.append(word)
                
        return ans