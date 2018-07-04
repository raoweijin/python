
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        size = 2*len(hashTable)
        hash =[None]*size
        
        for a in hashTable:
           if ( a != None) :
            p = a;
            while(p != None):
                hash = self.addNode(hash, p.val)
                p = p.next;        
        return hash
        
    def addNode(self,hashtable, member):
            size = len(hashtable)
            pos = hashtable[member%size];
            if (None == pos):
                pos = ListNode(member);
                hashtable[member%size] = pos;
            else:
                p = pos;
                while ( p != None):
                    if ( p.next == None):
                        p.next = ListNode(member);
                        break;
                    else:
                        p = p.next;
            return hashtable
    def printHash(self, hash):
        for i in hash:
            if(None != i):
                p = i
                while(p!= None):
                    print(p.val,end=" ")
                    p=p.next
                print("")
            else:
                print("None")

hash = [None]*3
mysol = Solution();
hash = mysol.addNode(hash, 3)
hash = mysol.addNode(hash, 6);
hash = mysol.addNode(hash, 7);
hash = mysol.addNode(hash, 8);
hash = mysol.addNode(hash, 10);
hash = mysol.addNode(hash, 16);
hash = mysol.addNode(hash, 13);
mysol.printHash(hash)
print("==============================")
hash = mysol.rehashing(hash)
mysol.printHash(hash)
'''        
        
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
        HASH_SIZE = 2 * len(hashTable)
        anshashTable = [None for i in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable,p.val)
                p = p.next
        return anshashTable
        
        '''