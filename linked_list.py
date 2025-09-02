from typing import List, Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return -1  # Return -1 if the index is out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        count = 0
        while current.next:
            if count == index - 1:
                current.next = current.next.next
                return True
            current = current.next
            count += 1
        return False  # Return False if the index is out of bounds

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

# Example usage:
linked_list = LinkedList()
linked_list.insertHead(1)
linked_list.insertTail(2)
linked_list.insertTail(3)
print(linked_list.getValues())  # Output: [1, 2, 3]
print(linked_list.get(1))       # Output: 2
linked_list.remove(1)
print(linked_list.getValues())




