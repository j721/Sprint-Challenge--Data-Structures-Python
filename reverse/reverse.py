class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    
    # def __str__(self):
    #     return f"{self}"

#Going to try Recursion
    def reverse_list(self, node, prev):

        #solution 1. Has more if and else statements

        #if the list is empty. No node present then return the list
        # if not node:
        #     return
        # #if list contains more than 1 node
        # #then call the recursion, and reverse through the first node and then the next node and so on
        # elif node.next_node is not None:
        #     self.reverse_list(node.next_node, node)
        # #else if the list only has one node the set the node to head    
        # else:
        #     self.head = node
        # #have the previous node become the new next node in the list
        # node.set_next(prev)

        #solution 2. Less if and else statements and more functions being called

        #if list is not empty. 
        if node is not None:
            #If the list only has 1 node. And there is no next node in the list
            #then set the node to head
            #have the next node from the head point to it as previous
            if node.get_next() == None:
                self.head = node
                self.head.next_node = prev
                return
            # #if list contains more than 1 node
            #then call the recursion, and reverse through the first node and then the next node and so on    
            self.reverse_list(node.get_next(), node)
             #have the previous node become the new next node in the list
            node.next_node = prev

# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.reverse_list(list.head, None)
# print(list)