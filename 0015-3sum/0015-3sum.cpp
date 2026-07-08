class Solution
{
    public:
        vector<vector < int>> threeSum(vector<int> &nums)
        {
            int n = nums.size();
            set<vector < int>> st;
            sort(nums.begin(), nums.end());
            for (int i = 0; i < n - 2; i++)
            {
                int l = i + 1, r = n - 1;
                while (l < r)
                {
                    int sum = nums[i] + nums[l] + nums[r];
                    if (sum == 0 && i != l && i != r && l != r)
                    {
                        st.insert({ nums[i],
                            nums[l],
                            nums[r] });
                        l++;
                        r--;
                    }
                    else if (sum < 0)
                    {
                        l++;
                    }
                    else
                    {
                        r--;
                    }
                }
            }
            vector<vector < int>> ans(st.begin(), st.end());
            return ans;
        }
};