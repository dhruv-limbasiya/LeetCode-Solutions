class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        mini = float('inf')
        for i in range(len(arr)-1):
            diff = 0
            diff = arr[i+1] - arr[i]
            mini = min(mini,diff)

        for i in range(len(arr)-1):
            diff2 = 0
            diff2 = arr[i+1] - arr[i]

            if diff2 == mini:
                ans.append([arr[i],arr[i+1]])
        
        return ans