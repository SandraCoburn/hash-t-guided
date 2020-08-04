class Node: #this corresponds to the HashEntryTable class
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: #this corresponds to the HashTable Class
    def __init__(self):
        self.head = None
    def find(self, value):
        #start at the head
        #loop through the list
        #find value
        #return the node
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.nex
        return None
    def delete(self, value):
        #find the index
        cur = self.head

        if cur.value == value:
            self.head = cur.nex
            return cur
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:
                self.head = cur.next
                return cur
            else:
                prev = cur
                cur = cur.next
        return None
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node 