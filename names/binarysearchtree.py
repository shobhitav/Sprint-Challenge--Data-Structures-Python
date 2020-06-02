

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if node to be inserted >= BST node
        if value >= self.value:
            if self.right: 
                # if there is a right node, consider it a root and recurse
                self.right.insert(value)
            else:
                # i there is no right node ,then create a node and add it 
                new_node= BSTNode(value)
                self.right = new_node
        elif value < self.value:
            if self.left:
                # if there is a left node, consider it a root and recurse
                self.left.insert(value)
            else:
                new_node=BSTNode(value)
                self.left = new_node
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target==self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False  
        else :
            if self.left:
                return self.left.contains(target)
            else:
                return False  


    # Return the maximum value found in the tree
    def get_max(self):
        # go right as far as we can go
        cur=self
        while cur.right is not None:
            cur=cur.right
        return cur.value    


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # calling function on current node
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
    # make a queue
    # queue=Queue()
    # queue.enqueue(node)

    # enqueue the node
    # as long as queue is not empty , this is current node
    # enqueue (put) the kids of current node on the queue
    # Check if they are not none and put them on queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # make a stack
        
        # push the node on stack
        # as long as the stack is not empty
        # pop of the stack, this is our current node
        # put the child of current node on the stack
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
