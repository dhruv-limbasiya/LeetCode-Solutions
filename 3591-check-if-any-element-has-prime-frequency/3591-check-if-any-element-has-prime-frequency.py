class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = {}

        for i in nums:
            freq[i] = nums.count(i)

        for i,j in freq.items():
            if j > 1:
                is_prime = True

                for k in range(2, j):
                    if j % k == 0:
                        is_prime = False

                if is_prime:
                    return True
                    
        return False                         