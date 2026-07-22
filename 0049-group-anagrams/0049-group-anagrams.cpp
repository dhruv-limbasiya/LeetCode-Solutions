class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        vector<vector<string>> ans;
        vector<bool> visited(strs.size(), false);

        // Precompute frequency of every string
        vector<vector<int>> freq(strs.size(), vector<int>(26, 0));

        for (int i = 0; i < strs.size(); i++) {
            for (char c : strs[i]) {
                freq[i][c - 'a']++;
            }
        }
        
        for (int i = 0; i < strs.size(); i++) {

            if (visited[i])
                continue;

            vector<string> temp;
            temp.push_back(strs[i]);
            visited[i] = true;

            for (int j = i + 1; j < strs.size(); j++) {

                if (visited[j])
                    continue;

                if (freq[i] == freq[j]) {
                    temp.push_back(strs[j]);
                    visited[j] = true;
                }
            }

            ans.push_back(temp);
        }

        return ans;
    }
};