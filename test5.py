data='abcd'
line=[]
res=[]
import copy
def dfs_palindrome(data):
    length = len(data)
    
    if length == 0 :
        resLine = copy.deepcopy(line)
        res.append(resLine)
        return
    
    for i in range(1, length+1):
        newData=data[i:]
        lineIe = data[:i]
        line.append(lineIe)
        #print(lineIe)
        dfs_palindrome(newData)
        line.pop()
        
def dfs_subset(data):
    length = len(data)
    
    if length == 0 :
        #resLine = copy.deepcopy(line)
        #res.append(resLine)
        return    
    for i in range(0, length):
        newData=data[i:]
        lineIe = newData[0]
        line.append(lineIe)
        newLIne = copy.deepcopy(line)
        res.append(newLIne)
        #print(lineIe)
        dfs_subset(newData[1:])
        
        #newLIne.append
        line.pop()
        

        
        
dfs_palindrome(data)
print(res)
line=[]
res=[]
data=['a','b','c']
subsetRes = dfs_subset(data)
print("subset",res)        