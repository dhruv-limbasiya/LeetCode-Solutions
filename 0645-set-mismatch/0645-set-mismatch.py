class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set1 = set()
        dup = 0

        for num in nums:
            if num in set1:
                dup = num

            set1.add(num)

        miss = -1    

        for i in range(1, len(nums)+1):
            if i not in set1:
                miss = i
                break

        return [dup, miss]              