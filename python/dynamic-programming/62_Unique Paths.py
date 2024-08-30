class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (n ==1) or (m == 1):
            return 1
        data = [1 for i in range(n)]
        for i in range(m-1):
            for j in range(1,n):
                data[j] = data[j] + data[j-1]
        return data[n-1]

    # Time limit exceeded
    def uniquePaths_failed(self, m: int, n: int) -> int:
        if (n ==1) or (m == 1):
            return 1
        else:
            return self.uniquePaths_failed(m-1, n) + self.uniquePaths_failed(m, n-1)



ans = Solution().uniquePaths(5,5)
print(ans)