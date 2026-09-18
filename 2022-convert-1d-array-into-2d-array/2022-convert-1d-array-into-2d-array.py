class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        ans = []
        
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[i * n + j])
            ans.append(temp)
        
        return ans