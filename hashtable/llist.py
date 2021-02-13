class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head

        # traverse the linked list
        while cur is not None:
            if cur.value == value:
                # found!
                return cur
            cur = cur.next
        
        return None
    
    def delete(self, value):
        cur = self.head

        # deleting the head of the list
        if cur.value == value:
            self.head = self.head.next
            return cur
        
        # normal case
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next == cur.next
                return cur
            else:
                prev = prev.next
                cur = cur.next
        
        return None
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(Node(21))

    print(ll.find(21))
    print(ll.find(11))
    print(ll.find(21))