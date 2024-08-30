import time

class Solution:   
    def numDecodings(self, s: str) -> int:
        if s == None or s[0] == '0':
            return 0
        
        dp1, dp2 = 1, 1
        for i in range(1,len(s)):
            # directly return case
            if (s[i-1:i+1] == '00') or (s[i] == '0' and s[i-1] > '2'):
                return 0
            
            if '1' <= s[i-1:i+1] <= '26' and s[i] != '0':
                dp1, dp2 = dp2, dp1+dp2
            elif s[i] == '0':
                dp1, dp2 = dp1, dp1
            else:
                dp1, dp2 = dp2, dp2
        return dp2


s = '4454'
ans = Solution().numDecodings(s)
print(ans)

arr = ['a', 'b', 'c', 'd']
for i, s in enumerate(arr):
    print(i, s)
