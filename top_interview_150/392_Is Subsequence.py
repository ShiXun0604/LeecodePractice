class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j =0, 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i +=1
            j +=1
        print(i ,j)
        return i == len(s)


s = 'abc'
t = 'ahbgdcee'
ans = Solution().isSubsequence(s, t)
print(ans)