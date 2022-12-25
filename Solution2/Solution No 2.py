class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l==1 or l==0:
            return
        for i in range(l//2):
            for j in range(i,l-1):
                matrix[i][j],matrix[j][l-1] = matrix[j][l-1], matrix[i][j]
                matrix[i][j],matrix[l-1][l-1-j+i] = matrix[l-1][l-1-j+i], matrix[i][j]
                matrix[i][j],matrix[l-1-j+i][i] = matrix[l-1-j+i][i], matrix[i][j]
            l-=1
        print(matrix)
R = int(input("Enter the number of rows of matrix:"))
C = int(input("Enter the number of columns of matrix:"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
    print()
Solution.rotate(Solution, matrix)