data=[8,1,7,9,6,5,10]
data=[7,8,9,1,2,3,4]
length = len(data)
num=[0 for i in range(0,length)]
sample=[[-1 for i in range(0,length)] for j in range(0,length)]
sample[0]= [data[0]]

for i in range(0,length):
    num[i]=1
max=-1
for i in range(0, length):
    for j in range(0,i):
        print(i,"; ",j," ")
        if(data[i]>data[j]):
            if(num[j]+1>num[i]):
                sample[i]=sample[j]+[data[i]]
            num[i]=max(num[j]+1,num[i])

        else:
            if(num[j]>num[i]):
                sample[i] = sample[j]
            elif(num[j]==num[i]):
                sample[i] = sample[j]
            num[i]=max(num[j],num[i])

print(data)
print (num)
print (sample)
