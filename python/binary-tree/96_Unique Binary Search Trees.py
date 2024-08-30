class Solution:
    def __init__(self) -> None:
        self.hash_table = {
            0 : 1,
            1 : 1,
            2 : 2,
        }
    def numTrees(self, n: int) -> int:
        if n in self.hash_table.keys():
            return self.hash_table[n]

        ans = 0
        for i in range(1,n+1):
            a = self.numTrees(i-1)
            b = self.numTrees(n-i)
            ans += a * b
        self.hash_table[n] = ans
        return ans


ans = Solution().numTrees(3)
print(ans)