a=[2,-6,4,-1,5,-9,6,-1,1,4,-5]
length = len(a)
maxSum=0
f=[None]*length

#def max(a,b)

f[0] = a[0]

    
for i in range(1, length):
    if(f[i-1]<0):
        f[i] = a[i]
    else:
        f[i]= f[i-1]+a[i]

        
print (f)        