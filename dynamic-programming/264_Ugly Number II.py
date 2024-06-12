class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index_2, index_3, index_5 = 0, 0, 0
        ans = [1]

        for i in range(n):
            num = min(ans[index_2]*2, ans[index_3]*3, ans[index_5]*5)
            ans.append(num)

            if num == ans[index_2]*2:
                index_2 += 1
            if num == ans[index_3]*3:
                index_3 += 1
            if num == ans[index_5]*5:
                index_5 += 1
        
        return ans[n-1]
            


n = 11
ans = Solution().nthUglyNumber(n)
print(ans)