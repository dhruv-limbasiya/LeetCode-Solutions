class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = left[i-1] + nums[i] 

        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + nums[i]

        for i in range(n):
            left_sum = left[i] - nums[i]
            right_sum = right[i] - nums[i]

            if left_sum == right_sum:
                return i

        return -1        