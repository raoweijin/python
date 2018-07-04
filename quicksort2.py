def quickSort2(alist):
    length = len(alist)
    if length<=1:
        return alist
    pivot = 0
    guard =alist[0]
    left = pivot
    right = length-1
    #leftflag = False
    righflag = True
    print("alist is ",alist)
    while left< right:                
        if righflag == True:
            if alist[right] >=guard:
                right-=1
            else:
                alist[pivot] = alist[right]
                alist[right] = guard
                pivot = right     
                print("pivot1: ",pivot)
                righflag = False
                #right-=1
        else:                  
            if alist[left] <= guard:
                left+=1
            else:
                alist[pivot] = alist[left]
                alist[left] = guard
                pivot = left
                print("pvivot2: ",pivot)
                #left+=1
                righflag = True
    print("id is ")
    for ie in alist:
        print(id(ie),end=" ")
    print("line")
   
    print("pivot3: ",pivot,"left: ",left, "right: ",right, "alias", alist) 
    alist[pivot] = guard
    print("pivot2: ",pivot,"left: ",left, "right: ",right) 
    
    if pivot +1 > length:
        print("except!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    quickSort2(alist[0:pivot])
    print("last alist1: ",alist)
    quickSort2(alist[pivot+1:length])
    print("last alist2: ",alist)
    return alist
data= [2,3,1,5,-1,0]

for ie in data:
    print(id(ie),end=" ")
print("line")
res = quickSort2(data)
print("res is ",res)
print("data is ",data)

def setNIe(a,i):
    if i>len(a)-1:
        return
    a[i]= 9
    setNIe(a,i+1)
    
data2=[8]
print("old data2 is ",data2)
setNIe(data2,0)
print("new data2 is ",data2)
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
   
data= [2,3,1,5,-1,0]
quickSort(data)
print("last data is ",data)