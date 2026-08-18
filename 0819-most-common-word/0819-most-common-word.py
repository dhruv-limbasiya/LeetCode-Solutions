import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      words = re.findall(r'\w+',paragraph.lower())

      words = [w for w in words if w not in banned]

      counts = Counter(words)

      return counts.most_common(1)[0][0]  