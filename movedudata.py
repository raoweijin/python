a=[0,2,2,3,4,4,5,5,8,9]
a=[1,1,4,2,2,3,3]
s=0
e=0
for i in range(0,len(a)-1):
    a[s] = a[i]
    
    if(a[i] != a[i+1]):
        s+=1
a[s] = a[len(a)-1]
print(a[0:s+1])