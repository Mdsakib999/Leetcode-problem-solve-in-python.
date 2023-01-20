class Solution:
    def minPathSum(self, grid: list) -> int:
        import ast

        getMatrix = input('Matrix : ')
        grid = ast.literal_eval(getMatrix)
        m = len(grid[0])
        n = len(grid)
        for i in range (1,n):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for i in range(1,m):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        for i in range (1,n):
            for j in range (1,m):
                grid[i][j] = min(grid[i][j] + grid[i-1][j] , grid[i][j] + grid[i][j-1])
        print("Answer= ",grid[-1][-1])


grid = []

print("Enter a matrix, use coma after each Entity; ")
result = Solution()

Solution.minPathSum(grid, result)





