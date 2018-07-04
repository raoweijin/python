class solution:
    def __init__(self):
        self.init=[1,2,3,4,5]
        
    def nthNum(self, n):
        if(n <=5):
            return self.init[n-1]
        i = 0
        j = 0
        data = {2,3,5}
        dataset={1,2,3,5}       
        res = 1
        while(1):
            if i< n-1:
                for ie in data:
                    #print("ie: ", ie)
                    if( j/ie in dataset):
                        
                        dataset.add(j)
                        i+=1
                        res = j
                        print("res: ",res)
                        if len(dataset) > 5:
                            dataset.pop([0])
                        break;
                j+=1
            else:
                break

        return res
                    
            
my =   solution()   
print(my.nthNum(9))   
         
        