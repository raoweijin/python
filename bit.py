a= 3
rightBit = 1 <<32
value = 0
num = 0
value= a & rightBit
while value ==0:
    
    
    rightBit = rightBit >> 1
    num+=1
    value= a & rightBit
    #print(rightBit,value)
print("num is ", num)
print("left num is ",32-num)
length = 32 - num
leftbit = 1
result = True
for i in range(length):
    rightvalue = a & rightBit
    leftvalue = a & leftbit
    leftbit = leftbit<<1
    rightBit = rightBit >>1
    if leftbit != rightBit:
        result = False
        break;
print("result is ", result)
   