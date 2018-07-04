class node:
    def __init__(self,val=None, next=None):
        self.val = val
        self.next = next

class List:
    def createList(self):
        nhead = node(0)
        print("nhead.next", nhead.next)
        temp = nhead
        temp.next = node(2)
        print("nhead.next", nhead.next)
        temp= temp.next
        temp.next = node(4)
        temp= temp.next
        temp.next = node(7)
        temp= temp.next
        temp.next = node(9)
        temp= temp.next
        temp.next = node(11)
        temp= temp.next
        return nhead
        
    def createList2(self):
        nhead = node(1)
        print("nhead.next", nhead.next)
        temp = nhead
        temp.next = node(3)
        print("nhead.next", nhead.next)
        temp= temp.next
        temp.next = node(5)
        temp= temp.next
        temp.next = node(10)
        temp= temp.next
        temp.next = node(12)
        temp= temp.next
        temp.next = node(13)
        temp= temp.next
        return nhead
    def printList(self,nHead):
        temp = nHead
        while temp != None:
            print(temp.val, end=" ")
            temp = temp.next
    
    def mergeTwoList(self,nHead1, nHead2):
        newHead1 = node(0); newHead1.next = nHead1; temp1 = nHead1;
        newHead2 = node(0); newHead2.next = nHead2; temp2 = nHead2;
        if temp1 == None:
            return nHead2;            
            
        if temp2 ==None:
            return nHead1;
        if temp1.val < temp2.val:
            res = temp1;
        else:
            res = temp2;
            
        while temp1.next != None:
            if temp2.next != None:
                if temp1.val > temp2.val:
                    temp2
            
        
        
        
def bubblesortNode(nHead):
    if nHead == None:
        return nHead;
        
    nTempNode = nHead
    nNum = 0
    while nTempNode.next != None:
        nTempNode = nTempNode.next
        nNum+=1
    nTail = nTempNode
    endNode = nTail
    nCur = nHead
    nFlag = False
    while nFlag == False:
        nFlag = True
        nCur = nHead
        while nCur.next != None:
            if nCur.val > nCur.next.val:
                nCur.val, nCur.next.val = nCur.next.val, nCur.val
                nFlag = False
            nCur = nCur.next 
            
    return nHead    
        
#def quicksortNode(nHead): 

myList = List()

nhead = myList.createList()

temp = nhead
myList.printList(nhead)

print("nhead2.next", nhead.next)
ntail= temp
#print("ntail ",ntail.val)
temp = nhead.next
temppre = nhead
temppre.next = None
#temppre.next = None
print("nhead.val", nhead.val)
tempnext = temp.next
while temp != None:
    #print(tempnext.val)
    temp.next = temppre
    temppre = temp
    temp = tempnext
    if None != tempnext:
        tempnext = tempnext.next
    
nhead = temppre
temp = nhead

print("converse list")
curNode = nhead
while curNode != None:
    if curNode.val == 2:
        tempNode = curNode.next;
        curNode.next = node(1)
        curNode.next.next = tempNode
        break
    curNode = curNode.next
temp = nhead        
print("inser node is")
myList.printList(nhead)

bubblesortNode(nhead)  
temp = nhead        
print("After sort")
myList.printList(nhead)



class Solution2(object):
    '''
    题意：合并两个有序链表
    '''
    def mergeTwoLists(self, l1, l2):
        dummy = node(999)
        tmp = dummy #PreviousNode
        while l1 != None and l2 != None:
            print("tmp.val is ",tmp.val)
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next
mysolut2 = Solution2()
list1 = myList.createList()
list2 = myList.createList2()
myList.printList(list1)
print("")
myList.printList(list2)
print("")
res = mysolut2.mergeTwoLists(list1,list2)
print("mergeTwoList-------------------------------")
myList.printList(res)