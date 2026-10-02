class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        w = m + n - 1
        a = m - 1
        b = n - 1

        while a >= 0 and b >= 0:
            if nums1[a] >= nums2[b]:
                nums1[w] = nums1[a]
                a -= 1
            else:
                nums1[w] = nums2[b]
                b -= 1

            w -= 1    
        
        while b >= 0:
            nums1[w] = nums2[b]
            b -= 1
            w -= 1            
