class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        asc_mapping = {}
        r_asc_mapping = {}
        for i in range(len(s)):
            if s[i] not in asc_mapping.keys():
                asc_mapping[s[i]] = t[i]
                r_asc_mapping[t[i]] = s[i]
            elif  asc_mapping[s[i]] != t[i]:
                return False
        
        if len(asc_mapping.keys()) != len(r_asc_mapping.keys()):
            return False
        return True


s = 'title'
t = 'paper'
solutuin = Solution()
ans = solutuin.isIsomorphic(s, t)
print(ans)