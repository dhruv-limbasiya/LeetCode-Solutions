class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence.lower()

        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in s:
                return False
        else:
            return True        