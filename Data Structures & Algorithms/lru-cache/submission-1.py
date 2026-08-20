class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}

        #dummy left and right node and attach the pointers
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):     #A <-> B <-> C    to    A <-> C
        #we have node to remove, so we find its neighbours and attach them
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        
    def insert(self, node):      
        #adds node C between B and self.right 
        #(A <-> B <-> self.right)  to (A <-> B <-> C <-> self.right)
        # Most Recently Used

        #identify where we want to insert the new node
        prev = self.right.prev  
        nxt = self.right

        #insert
        prev.next = node
        nxt.prev = node

        #pointers
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:

        #update at the right (MRU)
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]
        
