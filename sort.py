a=[2,4,3,6]
n = len(a)
flag = True

def sort(data, start, end):
    pos= start
    guard = data[pos]
    
    while(start<end):
        if(data[start] < data[pos]):
            start+=1
        if(data[end]  > data[pos]):
            end-=1
        
            
        