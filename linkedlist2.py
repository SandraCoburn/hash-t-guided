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
            cur = cur.next

        #if we get here, we didn't find it
        return None
    def insert_at_head(self, node):
        if self.head is None:
            node.next = None
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, value):
        #special case of deletingthe head of the list
        if self.head.value == value:
            old_head = self.head
            self.head = self.head.next
            return old_head
        #General case of deleting from the rest of the list
        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.value == value:
                #cut the node out
                prev.next = cur.next
                return cur
            else:
                prev = prev.next
                cur = cur.next
        #if we get here, we didn't find it
        return None
       
