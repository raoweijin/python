class perfectsquare:
    def squareAdd(self, data):
        flag= [99999]*(1+data)
        for i in range(0, 1+len(flag)):
            if(i*i<= data):
                flag[i*i] = 1
            else:
                break
        for i in range(0, data+1):
            for j in range(0,i):
                if((i-j*j)>=0):
                    print(i,j,i-j*j)
                    temp=flag[i-j*j]+1
                    if(temp< flag[i]):
                        flag[i] = temp
                
                
        return flag

        
mysolution = perfectsquare()
flag = mysolution.squareAdd(8)
print(flag)        