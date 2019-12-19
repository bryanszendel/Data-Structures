import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a tree/root
        if self.value == value:
            return
        if value < self.value:
            if self.left:
                # self.left = value
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right:
                # self.right = value
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return
        # else:
        #     self.value = value
        #     return
        # if value is less than self.value, go left, make a new tree/node if empty. 
        # Otherwise, keep going (recursion)
        
            
        # if greater than or equal to, then go right, make a new tree/node if empty. 
        # Otherwise, keep going (recursion)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # otherwise, left or right based on smaller or bigger
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                # self.value = value
                return self.left.contains(target)
            else: 
                return False 
        if target >= self.value:
            if self.right:
                # self.value = value
                return self.right.contains(target)
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise, return self.value

        if self.right:
            return self.right.get_max()
        else:
            return self.value
        # if self.right:
        #     self.value = self.right
        #     if self.right is None:
        #         return self.value
        #         # value = self.right
            
        # else:
        #     return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # hardest, use recursion.
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
