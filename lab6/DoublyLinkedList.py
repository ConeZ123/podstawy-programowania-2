class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def displayForward(self):
        if self.head == None:
            print("Lista jest pusta")
        else:
            current = self.head
            while current:
                print(current.data, end = " ")
                current = current.next

    def display_backward(self):
        if self.head == None:
            print("Lista jest pusta")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev

    def delete(self, data):
        if self.head == None:
            print("Lista jest pusta")
            return
        
        if self.head.data = data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        return

        current = self.head
        while current and current.data != data:
            current = current.next

        if current: 