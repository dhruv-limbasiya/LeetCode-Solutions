class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def get_rle(string: str) -> list[tuple[str, int]]:
            rle = []
            if not string:
                return rle
            i, n = 0, len(string)
            while i < n:
                char = string[i]
                j = i
                while j < n and string[j] == char:
                    j += 1
                rle.append((char, j - i))
                i = j
            return rle
        
        s_rle = get_rle(s)
        stretchy_count = 0
        
        for word in words:
            w_rle = get_rle(word)
            
            if len(s_rle) != len(w_rle):
                continue
                
            valid = True
            for (sc, sl), (wc, wl) in zip(s_rle, w_rle):
                if sc != wc or wl > sl:
                    valid = False
                    break
                if wl < sl and sl < 3:
                    valid = False
                    break
            
            if valid:
                stretchy_count += 1
                
        return stretchy_count