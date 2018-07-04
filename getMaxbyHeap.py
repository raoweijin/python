import heapq

data=[3,4,5,0,-1,-2]

a = []
b=[]
for ie in data:
    heapq.heappush(a,ie)

for ie in data:
    heapq.heappush(b,-ie)
 
min = heapq.heappop(a) 
max = (-1)*(heapq.heappop(b))

print("data is ",data)
print("min is ", min, "max is ",max)
