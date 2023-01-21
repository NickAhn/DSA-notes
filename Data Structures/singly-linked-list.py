class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
            self.head = self.tail = None
    
    def append(self, val) -> Node:
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode 
    
    # Prepend node to list and return new head
    def prepend(self, val) -> Node:
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        return self.head

    def insert(self, val, index) -> bool:
        if index > len(self):
            return False

        newNode = Node(val)
        i = 0
        prev = None
        cur = self.head
        while i < index:
            i+=1
            prev = cur
            cur = cur.next
        
        prev.next = newNode
        prev.next.next = cur
        return True
        
    def delete(self, val) -> Node:
        prev = None
        cur = self.head
        found = False
        while cur and not found:
            if cur.val == val:
                found = True
            else:
                prev = cur
                cur = cur.next
        
        if not found:
            return None
        # If previous is none, node to be deleted is head
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next

        return cur

    # If search is sucessful, return index position. Otherwise, None
    def search(self, val) -> int:
        index = 0
        cur = self.head
        while cur:
            if cur.val == val:
                return index
            index += 1
            cur = cur.next
        
        return -1

    def __str__(self) -> str:
        toString = ""
        cur = self.head
        while cur:
            toString += str(cur.val) + " "
            cur = cur.next
        return toString

    def __len__(self) -> int:
        cur = self.head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        return length