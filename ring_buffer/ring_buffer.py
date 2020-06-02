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
        #  if size equals to capacity, replace the oldest element (as per the index) with newest one
        else:
            # start from the beginning
            current = self.storage.head
            i = 0
            while current:
                # iterate and increment i until the oldest element is reached (when i equals to index)
                if i == self.index:
                    # replace the value of oldest element with new value
                    current.set_value(item)
                    # after replacement, now the next oldest element is at index+1
                    self.index += 1
                    # if after incrementing by 1, index grows to be equal to capacity, then use % to reset the index back to 0
                    self.index %= self.capacity
                    # break out of loop as we have already found and updated the oldest element
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
