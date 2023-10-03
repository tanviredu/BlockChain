#python
# Fully understand

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        ## checks if the linekd list is empty
        ## means head is None
        if self.head is None:
            self.head = new_node
        else:
            ## If the linked list is not empty
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data,end="=>")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
linked_list.prepend(0)
linked_list.display()
