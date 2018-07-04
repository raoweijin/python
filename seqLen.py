def findPos(data,target):
    length = len(data)
    if length ==0:
        return -1;
    if length == 1:
        if data[0] == target:
            return 0;
        else:
            return -1;
            
    start =0
    end  = length -1
    while start+1 < end:
        mid = (int)((start+end)/2)
        if data[mid] < target:
            start = mid;
        elif data[mid] == target:
            pos = mid;
            return pos
        else:
            end = mid
    if data[start] == target:
        return start;
    if data[end] == target:
        return end;
    return -1;
    

def findLeft(data,target):
    length = len(data)
    if length ==0:
        return -1;
    if length == 1:
        if data[0] == target:
            return 0;
        else:
            return -1;
            
    start =0
    end  = length -1
    print("start",start,end)
    while start+1 < end:
        mid = (int)((start+end)/2)
        print(start,end,mid)
        if data[mid] < target:
            start = mid;
        elif data[mid] == target:
            end = mid;            
        else:
            end = mid
    if data[start] == target:
        return start;
    if data[end] == target:
        return end;
    return -1;            
        
    
def findRight(data,target):
    length = len(data)
    if length ==0:
        return -1;
    if length == 1:
        if data[0] == target:
            return 0;
        else:
            return -1;
            
    start =0
    end  = length -1
    while start+1 < end:
        mid = (int)((start+end)/2)
        if data[mid] < target:
            start = mid;
        elif data[mid] == target:
            start = mid;            
        else:
            end = mid
    if data[end] == target:
        return end;
    if data[start] == target:
        return start;
    return -1;    
    
data =[0,1,2,2,2,2,4]
target = 2
print(data,target)
left = findLeft(data,target)
right = findRight(data,target)

print(left,right)