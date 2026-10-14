class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def findleft(nums, target):
            index = -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    index = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return index

        def findright(nums, target):
            index = -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    index = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return index

        return [findleft(nums, target), findright(nums, target)]                              