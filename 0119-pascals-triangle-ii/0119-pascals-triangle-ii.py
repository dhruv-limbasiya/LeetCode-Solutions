class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [[1]]

        for i in range(rowIndex):
            temp = [0] + result[-1] + [0]
            current = []

            for j in range(len(result[-1])+1):
                current.append(temp[j] + temp[j+1])

            result.append(current)    

        return result[rowIndex] 