import time

#need to implement a data structure to make search for names faster 
#going to try Binary Search Tree 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare the value to the root's value to determine which direction
            #we're gonna go in
            #if the value < root's value
        if value < self.value:
            #go left
            #how do we go left
            #we have to check if there is another node on the left side
            if self.left:
                #then self.left is a Node
                #moved the root from (self.left )and the .insert(value)- adds new value from the new root (self.left)
                self.left.insert(value)
            else:
                #then we can park the value here
                self.left = BSTNode(value)
        #else te value >= root's value
        else:
            if self.right:
                self.right.insert(value)
            else:
                    #then we can park the value here
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        #base case?
        #we find the target in the tree node
        if self.value == target:
            return True
        #figure out which direction we need to go in
        if target < self.value:
            #we go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        #or, we get a spot where the node should be, but nothing is there
        else: 
            #we go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        #how do we move towards the base case?
                

    # Return the maximum value found in the tree
    #used recursion - function that calls itself
    #run time O (log n)
    def get_max(self):
        #check to the right side of the tree
        #since left (self.left.value) side of the tree will always be smaller than the root

        #if the right side of the tree is empty that just return the tree
        if not self.right:
            return self.value
        #if right side of the tree is not empty. Then get the right child node with the max value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node

    #example of a tree traversal. Want to traverse through every tree node
    #recursion
    #doesn't actually return anything 
    def for_each(self, fn):
       #call the function `fn` on self.value
       fn(self.value)
        #go to right child nodes if any exists
       if self.right:
           self.right.for_each(fn)
       #go to the left child nodes if any exists
       if self.left:
           self.left.for_each(fn)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#create tree variable that will hold the BSTNode class and have index start at 0 for names_1 . 
# Since duplicates [] is a list that has an index when we have to loop through the name_2 file
tree = BSTNode(names_1[0])

#name and name2 are banana words
#but the names_1 and names_2 are the names of actual files

#create a loop where we will add a name into names_1
for name in names_1:
    tree.insert(name)
#create a loop for if tree contains a duplicate name
#then we will add that duplicate name into the duplicates array
for name2 in names_2:
    if tree.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
