class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])

        for num in freq:
            count = freq[num]
            bucket[count].append(num)

        result = []

        for count in range(len(nums), 0, -1):

            for num in bucket[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
