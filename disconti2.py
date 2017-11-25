data=[8,1,7,9,6,5,10]
data=[7,8,9,1,2,3,4,-100,-99,6,7]
data=[9]
data=[]
length = len(data)
num=[0 for i in range(0,length)]
res = [0 for i in range(0,length)]
sample=[[-1 for i in range(0,length)] for j in range(0,length)]
for i in range(0,length):
   for j in range(0,length):
       sample[i][j] = data[j]
sample=[[] for i in range(0,length)]
for i in range(0,length):
    num[i]=1
maxNum=-1
maxIndex=-1
if (1 ==len(data)):
    sample[0]= data[0]
    res[0]=data[0]
    maxIndexv = 0
else:
    for i in range(0, length):
        for j in range(0,i):
            print(i,"; ",j," ")
            if(data[i]>data[j]):
                if(1+num[j]>num[i]):
                    if(sample[j]==[]):
                        sample[j]=[data[j]]
                    sample[i] = sample[j]+[data[i]]
                num[i]=max(1+(num[j]),num[i])
    if(maxNum<num[i]):
        maxIndex = i
    maxNum = max(maxNum,num[i])
    res[i]=maxNum


print(data)
print (num)
print(res)
print(sample)
print(maxIndex)
print (sample[maxIndex])
#print (sample)
