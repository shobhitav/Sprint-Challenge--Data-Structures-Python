from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = self.storage.length

    def append(self, item):
        if self.storage.length<self.capacity:
            # add to tail
            self.storage.add_to_tail(item)
        else:
            # replace oldest element 
            self.storage.replace_at(self.current%self.capacity,item)
        self.current+=1
            
    def get(self):
        return self.storage.to_array()

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
