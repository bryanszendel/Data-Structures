import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.value = value
        if self.storage.__len__() == 0:
            self.storage.add_to_tail(self.value)
        else:
            self.storage.add_to_tail(value)
            return self.storage.tail.value

    def pop(self):
        if self.storage.__len__() == 0:
            return None
        elif self.storage.__len__() == 1:
            tailVal = self.storage.tail.value
            self.storage.remove_from_head()
            return tailVal
        else:
            tailVal = self.storage.tail.value
            self.storage.remove_from_tail()
            return tailVal

    def len(self):
        return self.storage.__len__()
