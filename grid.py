(row,collum)= (3,5)
grid= [[1 for i in range(0,collum)]for j in range(0,row)]
print (grid)
for i in range(1, row):
    for  j in range(1, collum):
        if((i!=0) and (j!=0)):
            grid[i][j]=grid[i-1][j]+grid[i][j-1]
for i in range(0, row):
    for  j in range(0, collum):			
        print("value is ", i," ",j," ",grid[i][j])