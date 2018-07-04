class linknode:
    def __init__(self, key=None, value=None,next=None):
        self.key = key  
        self.value = value;
        self.next = next;

class lrucache:
    def __init__(self, capacity):
        self.head = linknode()
        self.tail = self.head
        self.capacity = capacity
        self.hash = {}
        
    def get(self, key):
        if key not in self.hash:
            return None      
        result = self.hash[key].next.value        
        pre = self.hash[key]
        self.movenode(pre)
        return result
    
    def set(self, key, value):
        if key not in self.hash:
            node = linknode(key,value)
            self.pushback(node)
            if len(self.hash) > self.capacity:
                self.popfront()
        else:
            self.hash[key].next.value = value
        
    
    def popfront(self):
        del self.hash[self.head.next.key]
        head.next = head.next.next
        self.hash[head.next.key] = head
    
    def pushback(self, node):
        self.tail.next = node
        self.hash[node.key] = self.tail
        self.tail = node
    
    def movenode(self,pre):
        if( pre.next == self.tail):
            return
        node = pre.next
        
        pre.next = node.next
        self.hash[node.next.key] = pre
        node.next = None
        self.pushback(node)
mycache = lrucache(5)        
mycache.set("jessie",9)
mycache.set("cathy",36)
mycache.set("jim",40)

print(mycache.head.next.value)
print(mycache.tail.value)
print(mycache.get("cathy"))

    
    