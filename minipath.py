miniPath[0][0]= data[0][0]
for i in range(0, collum):
    for j in range(0, row):
        miniPath[i][j]=data[i][j]*min(miniPath[i-1][j],miniPath[i][j-1])
return