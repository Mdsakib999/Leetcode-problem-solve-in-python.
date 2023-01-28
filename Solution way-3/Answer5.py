Rows = int(input("Enter rows:"))  
Columns = int(input("Enter columns:"))  
  
lis = []  
print("Enter row-wise:")  
  
for a in range(Rows):   
    r = []  
    for b in range(Columns): 
        r.append(int(input()))  
    lis.append(r)  
  
for a in range(Rows):  
    for b in range(Columns):  
        print(lis[a][b], end=" " )
    print()

indexData = set() 
for row in range(len(lis)): 
    for column in range(len(lis[0])): 
        if lis[row][column] == 0: 
            indexData.add(row) 
            indexData.add(column) 
for row in range(len(lis)): 
    for column in range(len(lis[0])): 
        if row in indexData or column in indexData: 
            lis[row][column] = 0 
            
print("Output:",lis)