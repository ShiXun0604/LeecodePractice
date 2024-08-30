class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # edge case
        if obstacleGrid == None or obstacleGrid[0][0] == 1:
            return 0
        
        # border length
        I = len(obstacleGrid)
        J = len(obstacleGrid[0])

        point_grid = [[0]*J for a in range(I)]
        point_grid[0][0] = 1
        for i in range(I):
            for j in range(J):
                if obstacleGrid[i][j] == 0:
                    if i >= 1:
                        point_grid[i][j] += point_grid[i-1][j]
                    if j >= 1:
                        point_grid[i][j] += point_grid[i][j-1]
        
        return point_grid[I-1][J-1]


# test
solution = Solution()
obstacleGrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ans = solution.uniquePathsWithObstacles(obstacleGrid)
print(ans)