#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addlistnode(self, node, number):
        if node.next != None:
            self.addlistnode(node.next, number)
        else:
            node.next = ListNode(number)

    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] == None:
            anshashTable[p] = ListNode(number)
        else:
		
            self.addlistnode(anshashTable[p], number)

    def rehashing(self,hashTable):
        anshashTable = [None for i in range(len(hashTable) * 2)]
        HASH_SIZE = 2 * len(hashTable)
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable,p.val)
                p = p.next
        return anshashTable
		
hashTable=[None,None,None]
myHashFunc = Solution()
myHashFunc.addnode(hashTable,2)
myHashFunc.addnode(hashTable,5)
Solution(,hashTable,5)
print(hashTable)	
print(hashTable[2].val)	
print(hashTable[2].next.val)	