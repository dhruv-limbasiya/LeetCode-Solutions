from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        waiting = defaultdict(list)
        
        for word in words:
            it = iter(word)
            first_char = next(it, None)
            if first_char:
                waiting[first_char].append(it)
                
        match_count = 0
        
        for char in s:
            current_waiting = waiting[char]
            waiting[char] = []
            
            for it in current_waiting:
                next_char = next(it, None)
                if next_char is None:
                    match_count += 1
                else:
                    waiting[next_char].append(it)
                    
        return match_count