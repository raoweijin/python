class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        dataSet = set(num)
        #for ie in num:
        #    dataSet.add(ie)
        print("dataset is ",dataSet)
         
        res = 0
        for ie in set(dataSet):
            print("tempset is ",set(dataSet),"res is ",res,)
            #res = 1
            dataSet.discard(ie)
            #l = ie-1
            data = [ie]
            l= ie-1
            while l in dataSet:
                data.insert(0,l)
                dataSet.discard(l)
                l-=1
            r = ie+1
            while r in dataSet: 
                data.append(r)
                dataSet.discard(r)
                r=r+1
            print("data is ",data)
            res = max(res, r-l-1)
        return res
                
data=[1,7,4,2,3,10,10,99,2,5,11,6,9,12,13,56,14,4715,88,15,16]    
mySol = Solution()
res = mySol.longestConsecutive(data)
print("res is ",res)
    
'''
# O(n)
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        dict={}
        
        for x in num:
            dict[x] = 1
            
        ans = 0
        
        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1 
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len
                    
        return ans
        

# O(nlogn)
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        l = num[0] 
        ans = 1
        tmp = 1
        for n in num:
            if(n - l == 0):
                continue;
            elif(n - l == 1):
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
            l = n
        if tmp > ans:
            ans = tmp
        return ans
'''