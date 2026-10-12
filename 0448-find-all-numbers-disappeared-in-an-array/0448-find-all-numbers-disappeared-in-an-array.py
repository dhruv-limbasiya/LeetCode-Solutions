class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        ans = []    

        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
                
        return ans        