class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        map<char,int>ss;
        map<char,int>tt;

        for(auto i : s){
            ss[i]++;
        }
        for(auto i : t){
            tt[i]++;
        }

        return ss == tt;
    }
};