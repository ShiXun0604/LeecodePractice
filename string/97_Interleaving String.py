class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a, b =0, 0
        for i in s3:
            print(i ,a , b)
            if a < len(s1) and i == s1[a]:
                a += 1
            elif b < len(s2) and i == s2[b]:
                b += 1
            else:
                return False
        return True



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
ans = Solution().isInterleave(s1, s2, s3)
print(ans)