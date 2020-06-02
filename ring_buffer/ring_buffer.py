class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        else:
            self.head = new_node

        self.size += 1


class RingBuffer:
    def __init__(self, capacity):
        self.storage=LinkedList()
        self.capacity=capacity
        self.index = 0
    
    def append(self, item):
        # if size is less than capacity keep adding to tail
        if self.storage.size < self.capacity:
            self.storage.add_to_tail(item)
        #  if size equals to capacity, replace the oldest element with newest one
        else:
            current = self.storage.head
            i = 0
            while current:
                if i == self.index:
                    current.set_value(item)
                    self.index += 1
                    # to reset the index ie to find the correct index which is oldest one 
                    self.index %= self.capacity
                    break
                i += 1
                current = current.get_next()

    def get(self):
        retArr = []
        current = self.storage.head
        while current:
            retArr.append(current.get_value())
            current = current.get_next()
        return retArr
