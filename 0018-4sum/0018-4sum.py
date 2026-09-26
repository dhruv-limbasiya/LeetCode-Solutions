class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                p = j+1
                q = n-1

                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]

                    if s < target:
                        p +=1 
                    elif s > target:
                        q -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1

                        while p < q and nums[p] == nums[p-1]:
                            p+=1
   
        return ans                
