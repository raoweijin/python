a=[1,2,3,4,5]
size=3
class listNode:
    def __init__(self,value=None,next=None):
        #self.key=key
        self.value=value
        self.next=None

head = listNode()
work = head
for i in a:
    work.next =listNode(i)
    work = work.next

point = head
while(point != None):
    print(point.value)
    point = point.next
        

winstart=head.next
num = 0
winSize = 3
point = head
while ((point != None) and (num< winSize)):
    point = point.next
    num = num + 1
winEnd = None
if (point != None):
    winEnd = point

winSum=[]

temp = 0
while(winEnd != None):
    point = winstart
    for i in range(winSize):
        temp = temp+ point.value
    winSum = winSum + [temp]
    temp = 0
    winstart = winstart.next
    winEnd = winEnd.next
print (winSum)
    