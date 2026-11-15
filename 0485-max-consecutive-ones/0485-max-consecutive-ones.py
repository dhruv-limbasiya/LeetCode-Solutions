class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
                maxi = max(c, maxi)

            else:
                c = 0

        return maxi                    
