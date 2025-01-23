# Linked List ====================

# Single Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")
# =================================================================

# Double Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\nTraversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

# ======================================================
class Node:
    def  __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(2)
node2 = Node(55)
node3 = Node(53)
node4 = Node(11)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

currentNode = node1
while currentNode:
    print(currentNode.data,end="->")
    currentNode =currentNode.next
print("NUll")


currentNode = node4
while currentNode:
    print(currentNode.data,end="<-")
    currentNode =currentNode.prev
print("NUll")

# ===========================================================================
# Find min value in linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
minValue = node1.data
while currentNode:
    if currentNode.data < minValue:
        minValue = currentNode.data
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")
print(minValue)

# ===================================================================
# Delete a node in linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def deleteSpecificNode(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode:
        if currentNode.next ==  nodeToDelete:
            currentNode.next = currentNode.next.next
        currentNode = currentNode.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3 
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

# =================================================================
class Node:
    def __init__(self,data):
        self.data = data 
        self.next =None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def insertionnode(head,newnode,position):
    if position == 1:
        newnode.next = head
        return newnode
    currentnode = head
    for _ in range(position -2):
        if currentnode is None:
            break
        currentnode = currentnode.next

    newnode.next = currentnode.next
    currentnode.next = newnode
    return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newnode = Node(97)
node1 = insertionnode(node1, newnode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)

# ===================================================================
# bubble sort using linked list
class Node:

    def __init__(self,data):
        self.data = data
        self.next  =None
        
class sorting:
    def __init__(self):
        self.head = None

    def bubblesort(self):
        end = None
        
        while self.head != end:
            current = self.head
            while current.next != end:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data , current.data
                current = current.next
            end =current

    def display(self):
        current =self.head
        while current:
            print(current.data,end="->")
            current =current.next
        print("None")

node1 =Node(4)
node2 = Node(3)
node3 = Node(1)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

sorting_obj = sorting()
sorting_obj.head = node1

sorting_obj.bubblesort()

sorting_obj.display()

# ======================================================================# Python program for merge sort on singly linked list
# merge Sort 
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def split(head):
    fast = head
    slow = head

    # Move fast pointer two steps and slow pointer
    # one step until fast reaches the end
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next

    # Split the list into two halves
    second = slow.next
    slow.next = None
    return second

def merge(first, second):
  
    # If either list is empty, return the other list
    if not first:
        return second
    if not second:
        return first

    # Pick the smaller value between first and second nodes
    if first.data < second.data:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second

def merge_sort(head):
  
    # Base case: if the list is empty or has only one node, 
    # it's already sorted
    if not head or not head.next:
        return head

    # Split the list into two halves
    second = split(head)

    # Recursively sort each half
    head = merge_sort(head)
    second = merge_sort(second)

    # Merge the two sorted halves
    return merge(head, second)

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Create a hard-coded singly linked list:
    # 9 -> 8 -> 5 -> 2
    head = Node(9)
    head.next = Node(8)
    head.next.next = Node(5)
    head.next.next.next = Node(2)

    head = merge_sort(head)
    print_list(head)


