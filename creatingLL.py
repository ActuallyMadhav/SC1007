class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' --> ')
            current = current.next
        print("None")
    
    def findAt(self, index):
        current = self.head
        if not current:
            return None
        while index > 0:
            current = current.next
            if not current:
                return None
            index -= 1
        return current
    
    def insert_at_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        new_node = Node(data)

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True
        
        current = self.head
        count = 0

        while current and position < index - 1:
            current = current.next
            count += 1

        if not current:
            print("Index out of range")
            return False
        
        new_node.next = current.next
        current.next = new_node
        return True

    def size(head):
        #initialize counter
        count = 0

        #start at head
        current = head

        #traverse the list
        while current is not None:
            count += 1 #increase counter
            head = head.next #move to next node
        return count

    def findNode(head, index):
        if head is None or index < 0:
            return None
        cur = head
        while index > 0:
            cur = cur.next
            if cur is None:
                return None
            index -= 1
        return cur

    def findNode2(ll, index):
        if ll.head is None or index < 0 or index >= ll.size:
            return None
        
        cur = ll.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(head, index, item):
        newNode = ListNode(item)
        if head is None:
            return newNode
        if index == 0:
            newNode.next = head
            return newNode
        prev = findNode(head, index - 1)
        if prev is not None:
            newNode.next = prev.next

    def insertNode2(head, index, item):
        newNode = ListNode(item)

        #scenario 1: inserting into an empty list
        if head is None:
            if index == 0:
                head = newNode
                return True
            return False
        
        #scenario 2: inserting at beginning of non empty list
        if index == 0:
            newNode.next = head
            head = newNode
            return True
        
        #scenario 3: inserting in middle or end of list
        prev = findNode(head, index - 1)
        if prev is not None:
            newNode.next = prev.next
            prev.next = newNode
            return True
        return False

if __name__ == "__main__":

 # Initialize empty linked list object
    linked_list = LinkedList()

 # Create nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

 # Link nodes
    linked_list.head = node1
    node1.next = node2
    node2.next = node3

 # Print the linked list
 # Passes linked_list.head as argument
    linked_list.display()
