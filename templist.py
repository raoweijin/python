class node:
    def __init__(self,val=None, next=None):
        self.val = val
        self.next = next
        
    def __del__(self):
        print("I will delete myself")

def createlist():
    nHead = node(0)
    nHead.next = node(1)
    return nHead
    
        
def printList(nHead):
    temp = nHead
    while temp != None:
        print(temp.val, end=" ")
        
        p = temp.next
        del temp
        temp = p      
    print("")
    print("delete end")
        
nHead=createlist();
printList(nHead)
print("the program will die")