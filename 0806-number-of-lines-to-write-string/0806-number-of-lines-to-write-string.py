class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        current_width = 0

        for c in s:
            width = widths[ord(c) - ord('a')]

            if width + current_width > 100:
                line += 1
                current_width = 0
            
            current_width += width
        
        return [line, current_width]
        