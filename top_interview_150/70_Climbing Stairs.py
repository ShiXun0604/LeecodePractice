class Solution:
    def climbStairs(self, n: int) -> int:
        def C(i, j):
            j = min(j, i-j)
            result = 1
            for a in range(j):
                result *= (i-a)
                result /= (a+1)
            return int(result)
        
        num_1 = n
        num_2 = 0

        ans = 0
        while num_1 >= 0:
            ans += C(num_1+num_2, num_1)
            num_1 -=2
            num_2 +=1
        
        return ans


solution = Solution()
solution.climbStairs(5)
