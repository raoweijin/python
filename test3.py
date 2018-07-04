import copy
class Solution:
    def split(self, data):
        length = len(data)
        
        res = [[] for i in range(0,length)]
        res[0] = [[data[0]]]
        
        for id in range(1,length):
            ie= data[id]
            #print("ie: ",ie)
            res[id]= self.merge(res[id-1],ie)
        
        return res
    #Dynnamic programing. f[n] = f[n-1].append(a[n]) + f[n-1].insert(a[n])
    def merge(self, nlist,newInput):
        #res =copy.deepcopy(nlist)
        res=[]
        for id, ie in enumerate(nlist):
            temp = copy.deepcopy(ie)
            temp.append(newInput)
            res.append(temp)
            temp = copy.deepcopy(ie)
            temp[-1]= temp[-1]+newInput
            #print(temp)
            res.append(temp)
        return res
    def dfs(self,data, line):
        res = []        
        length = len(data)
        if 0 == length:
            res.append(line)
        else:        
            for i in range(1,length):
                dfs(data,i, line)
        return res
data= 'rwj'
print(data)
mysolution = Solution()
res = mysolution.split(data)
print(res)
length = len(data)
print("resut is ",res[length-1])
           
     
            
            
        