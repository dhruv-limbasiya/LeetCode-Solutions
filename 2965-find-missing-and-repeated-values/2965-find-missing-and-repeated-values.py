class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid)
        total = n * n

        temp = []

        for i in range(n):
            for j in range(n):
                num = grid[i][j]

                if num not in temp:
                    temp.append(num)
                else:
                    ans.append(num)

        for num in range(1, total + 1):
            if num not in temp:
                ans.append(num)

        return ans