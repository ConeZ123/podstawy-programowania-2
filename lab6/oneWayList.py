class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SlinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = none
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        if head == None:
            print("Lista jest pusta")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def delete(self, data):
        if self.head == None:
            print("Lista jest pusta")
            break

        if self.head.data == data:
            self.head = self.head.next
            break
        
        current = self.head
        prev = None
        while current:
            if current.data = data:
                prev.next = current.next
                return
            prev = current
            current = current.next
