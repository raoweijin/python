a=[6,1,2,3,9,4,8,5]
a=[1,3,2,4]
#a=[2,1]

global num
num = 0

#def quicksort2(data,start,end):
    
    
    

def quicksort(data,start, end):

    print(data)
    print(start,end)
    guard_pos = start
    if(start>=end):
        return data[start:start+1]
    first = start
    last = end
    while(first< last):
        global num
        num+=1
        print ("num is ", num)
        if(first < guard_pos):
            if(data[first]>data[guard_pos]):
                (data[first],data[guard_pos]) = (data[guard_pos],data[first])
                guard_pos = first
            first+=1    
        if(last > guard_pos):
            if(data[last] < data[guard_pos]):
                (data[last],data[guard_pos])= (data[guard_pos],data[last])
                guard_pos = last;
            last-=1
    d1 = quicksort(data,start, guard_pos)        
    d2 = quicksort(data,guard_pos+1, end)
    return d1+d2


def swap(left, right):
    temp = left
    left = right
    right = temp
'''    
def quicksort(data,start, end):
    guard = start
    sa= start
    ea = end
    sa_falg = 0
    ea_flag = 0
    print("start, end is ", start, end)
    print("data is ",end='')
    for i in range(start,end+1):
        print(data[i], end=' ')
    print('\n')
    if(start+1 >=end):
        print("return")
        return
    while(sa<ea):
        print(sa,ea)
        if(data[sa]<=data[guard]):
            sa+=1
            sa_flag = 0
        else:
            sa_falg=1
        if(data[ea]>=data[guard]):
            ea-=1
            ea_flag = 0
        else:
            ea_flag= 1
        if((ea_flag ==1) and (sa_falg ==1)):
            #swap(data[sa],data[ea])
            (data[sa],data[ea]) = (data[ea],data[sa])
            sa_falg = 0
            ea_flag = 0
            sa+=1
            ea-=1
    quicksort(data,start,sa-1)
    quicksort(data,ea,end)
'''
length = len(a)
print("length is ", length)
a2 = quicksort(a,0,length-1)
print(a2)