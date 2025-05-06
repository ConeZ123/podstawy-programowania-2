# Drzewa binarne
# Drzewo binarne to struktura danych, w której każdy węzeł ma co najwyżej dwóch potomków (lewego i prawego)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# lista [3, 5, 7, 10, 20]
root = Node(10)
root.left = Node(5)
root.left = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print("Wartość korzenia: ", root.value)
print("Wartość lewego dziecka", root.left.value)
print("Wartość prawego dziecka", root.right.value)

# drzewo BST
# BST (Binary Search Tree) to szczególny rodzaj drzewa binarnegom w którym dla każdego węzła:
# - wartośc lewego pomtomka jest mniejsza od wartości węzła
# - wartość prawego potomka jest większa od wartości węzła

class NoteBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = NodeBST(new_value)
                self.parent = self
            else:
                self.left = insert(new_value)
        else:
            if self.right is None:
                self.right = NodeBST(new_value)
                self.parent = self
            else:
                self.right.insert(new_value)

    def search(self, search):
        if search == self.value:
            return self
        elif search < self.value and self.left is not None:
            return self.left.search(search)
        elif search > self.value and self.right is not None:
            return self.right.search(search)
        return None

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)

        else:
            # usuniecie wezla
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                self.left.parent = self.parent
                return self.right
            elif self.right is None:
                self.right.parent = self.parent
                return self.left
            else:
                # wezel z dwoma dziecmi
                min_node = self.right.find_min()
                self.value = min_node.value
                self.right = self.right.delete(min_node.value)
        return self