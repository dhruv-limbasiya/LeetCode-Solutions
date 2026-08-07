class Solution
{
    public:
        double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2, nums1);
        int l = 0; int r = m;
        while (l <= r) {
            int part1 = (l + r) / 2;
            int part2 = (m + n + 1) / 2 - part1;
            int maxL1 = part1 == 0 ? INT_MIN : nums1[part1-1];
            int minR1 = part1 == m ? INT_MAX : nums1[part1];
            int maxL2 = part2 == 0 ? INT_MIN : nums2[part2-1];
            int minR2 = part2 == n ? INT_MAX : nums2[part2];
            if (maxL1 <= minR2 && maxL2 <= minR1) {
                if ((m+n) % 2 == 0) {
                    return (double(max(maxL1, maxL2)) + double(min(minR1, minR2))) / 2.0;
                } else {
                    return double(max(maxL1, maxL2));
                }
            } else if (maxL1 > minR2) {
                r = part1 - 1;
            } else {
                l = part1 + 1;
            }
        }
        return 0.0;  // so it compiles
    }
}; 
