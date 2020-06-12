#Notes from Readme

# ring buffer is a non-growable buffer with a fixed size. 
#also known as a circular Queue. FIFO (first in first out) order
# When the ring buffer is full and a new element is inserted, 
# the oldest element in the ring buffer is overwritten with the newest element. 

#  useful for use cases such as storing logs and history information,
#  where you typically want to store information up until it reaches a certain age,
#   after which you 
#   don't care about it anymore and don't mind seeing it overwritten by newer data.

#  The append method adds the given element to the buffer. 
#  The get method returns all of the elements in the buffer in a list in their given order.
#  It should not return any None values in the list even if they are present in the ring buffer.

class RingBuffer:
    def __init__(self, capacity):
        #need to initialize ring buffer. Set it None to be empty. 
        self.capacity = capacity
        self.storage = [None] *capacity
        #set current node/element value to 0
        self.current = 0

    def append(self, item):
        #first item with index of 0 becomes the oldest node
        #appends an element overwriting the oldest element by increments of +1
        self.storage[self.current] = item
        self.current +=1
        #if current value of element reaches the limit/full capacity of ring buffer. Then set current to 0
        if self.current == self.capacity:
            self.current = 0

      
    def get(self):
        #loops through the self.storage in ring buffer to return new values
        return [val for val in self.storage if val is not None]

        #return self.storage    