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
        temp.next = node(3)
        temp= temp.next
        temp.next = node(5)
        temp= temp.next
        temp.next = node(6)
        temp= temp.next
        return nhead
    def printList(self,nHead):
        temp = nHead
        while temp.next != None:
            print(temp.val, end=" ")
            temp = temp.next
    def reverseList(self, nHead):
        newhead=node(0); newhead.next=nHead
        while newhead.next!=None:
            tmp=nHead.next
            nHead.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return newhead
            
            
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        # Write your code here
        newhead=ListNode(0); newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
    def reverseKGroup(self, head, k):
        if head==None: return None
        nhead=ListNode(0); nhead.next=head; start=nhead
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None: return nhead.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]
            start=res[1]
        return nhead.next
myList = List()
nHead = myList.createList()
myList.printList(nHead)
print("dddddddddddddddddddddddddd")
newHead = myList.reverseList(nHead)
myList.printList(newHead)
    


        
