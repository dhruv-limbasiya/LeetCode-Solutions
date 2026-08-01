class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set()

        for i in nums:
            ans.add(i)

        miss = []

        for i in range(1, len(nums)+1):
            if i not in ans:
                miss.append(i)

        return miss        