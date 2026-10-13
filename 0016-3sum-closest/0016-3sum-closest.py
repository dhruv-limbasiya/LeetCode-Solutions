class Solution:
    def threeSumClosest(self, arr, target):
        arr.sort()

        resultSum = arr[0] + arr[1] + arr[2]
        minDifference = float('inf')

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                sum_val = arr[i] + arr[left] + arr[right]

                if sum_val == target:
                    return sum_val

                diffToTarget = abs(sum_val - target)

                if diffToTarget < minDifference:
                    resultSum = sum_val
                    minDifference = diffToTarget

                if sum_val < target:
                    left += 1
                else:
                    right -= 1

        return resultSum