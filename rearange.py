a="AEBCFD2HI3JK"
a=[2,0,3,1,5,4,19,6,9,8,-1]
a=['A','9','7','B','0','Z','8','F','5','E','8','X','6','7']
length=len(a)
print("length",length)
start=0
end = 0
data=0
for j in range(length):
    print(a,start,end,data,a[start],a[end])
    a[start] = a[end]
    if(a[start]>'9' or a[start]<'0'):
        start+=1
    else:
        data+=(ord(a[start])-ord('0'))

    end+=1
    
for j in range(start-1):
    print(a)
    for i in range(0,start-j-1):    
        if(a[i]>a[i+1]):
            temp=a[i+1]
            a[i+1] = a[i]
            a[i]= temp
a[start]=data
for j in range(start+1,length):
    a[j] = 0
print(a)            