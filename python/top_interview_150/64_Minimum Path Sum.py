# 自己想可行但是時間複雜度太高的解法(divide and conquer)
'''
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    if m == 1:
        num = 0
        for i in range(n):
            num += grid[0][i]
        return num
    
    if n == 1:
        num = 0
        for i in range(m):
            num += grid[i][0]
        return num
    
    grid1 = grid[1:]
    grid2 = []
    for row in grid:
        grid2.append(row[1:])

    return min(minPathSum(grid1), minPathSum(grid2))+grid[0][0]
'''

# 參考別人的寫法
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    for i in range(1, n):
        for j in range(1, m):
            grid[j][i] += min(grid[j-1][i], grid[j][i-1])
    
    return grid[m-1][n-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))

