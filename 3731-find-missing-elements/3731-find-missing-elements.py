class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        maxx = max(temp)
        mini = min(temp)
        ans = []

        for i in range(mini,maxx):
            if i not in temp:
                ans.append(i)

        return ans