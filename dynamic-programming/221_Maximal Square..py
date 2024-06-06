class Solution:
    # Needs improve(execute time is too long)
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ans = int(matrix[0][0])

        for i in range(1, len(matrix)):
            if matrix[i][0] == '1':
                ans = 1
                break
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == '1':
                ans = 1
                break
    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j-1]) and int(matrix[i-1][j]) and int(matrix[i-1][j-1]) and int(matrix[i][j]):
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
                ans = max(ans, int(matrix[i][j]))
                print(int(matrix[i][j]), end=' ')
            print()
        return ans**2
