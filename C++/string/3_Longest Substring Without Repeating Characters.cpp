#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.size();
        int sq[128] = {0};
        int mx = 0;
        for (int l=0, r=0; r<len; r++){
            l = max(sq[s[r]], l);
            mx = max(mx, r - l + 1);
            sq[s[r]] = r + 1;
        }
        return mx;
    }
};



int main(){
    Solution sol;
    int ans = sol.lengthOfLongestSubstring("abcabcbb");
    cout << ans << endl;
    return 0;
}