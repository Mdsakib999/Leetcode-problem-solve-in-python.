class Solution:
    def min_path_sum(self, grid:list) -> int:
        m = len(grid[0])
        n = len(grid)
        for i in range (1,n):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for i in range(1,m):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        for i in range (1,n):
            for j in range (1,m):
                grid[i][j] = min(grid[i][j] + grid[i-1][j] , grid[i][j] + grid[i][j-1])
        print("Answer = ",grid[-1][-1])


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
# Initialize matrix
grid = []
print("Enter the Matrix:")
  
# For user input
for i in range(R):         
    a =[]
    for j in range(C):      
         a.append(int(input()))
    grid.append(a)
    print()
  

print("Sum = ",grid)
Solution.min_path_sum(Solution, grid)
