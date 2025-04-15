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
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        if self.head == None:
            print("Lista jest pusta")
        else:
            current = self.head
            while current:
                print(current.data, end = " ")
                current = current.next

    def delete(self, data):
        if self.head == None:
            print("Lista jest pusta")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next


lista = SlinglyLinkedList()
lista.append(15)
lista.append(25)
lista.append(35)
lista.display()

lista.delete(25)
lista.display()

lista.delete(15)
lista.display()