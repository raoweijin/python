import heapq
a=[]
heapq.heappush(a,1)
heapq.heappush(a,3)
heapq.heappush(a,2)
print(a)
k=heapq.heappop(a)
print(k)
print("a ",a)
k=heapq.heappop(a)
print(k)
print("a ",a)
k=heapq.heappop(a)
print(k)