def divident(data,start,length,wordList ,res):
    #length = len(data)
    print("length is ", length)
    if length == 0:
        res.append(wordList)
        return 
    for i in range(start+1,start+length):
        temp = data[start:i]
        wordList = wordList+ temp        
        data_temp = data[i:]
        print("wordlist is", wordList, " i is ",i," data is ",data_temp)
        newLength = length - i
        newStart = start + i
        divident(data_temp,newStart,newLength,wordList,res)
data =[1,2,3]
print("data is ",data)
res=[]
wordList =[]
length = len(data)
divident(data,0, length,wordList,res)

print("res is ", res)
        
