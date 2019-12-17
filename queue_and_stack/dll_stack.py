import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.value = value
        if self.storage.__len__() == 0:
            self.storage.add_to_tail(self.value)
            # self.storage.add_to_tail(value)
        # return self.storage.tail.value
        # elif self.storage.__len__() is None: 
        #     return None
        else:
            self.storage.add_to_tail(value)
            return self.storage.tail.value

    def pop(self):
        # print('STORAGE', self.storage.__len__())
        if self.storage.__len__() == 0:
            return None
        elif self.storage.__len__() == 1:
            tailVal = self.storage.tail.value
            self.storage.remove_from_head()
            return tailVal
        # elif self.storage.__len__() is None:
        #     return None
        # else:
            # returnVal = self.storage.tail.value
        else:
            tailVal = self.storage.tail.value
            self.storage.remove_from_tail()
            return tailVal
        # return self.storage.tail.value

    def len(self):
        # print(self.storage.__len__())
        return self.storage.__len__()
