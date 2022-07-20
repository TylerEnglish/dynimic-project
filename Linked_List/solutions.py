class Node:
    '''
    Create the ability to 
    make a linked list
    '''
    def __init__(self, data):
        self.data = data
        self.next = None
def detect_loop(head):
    '''
    find out if there's a loop 
    in the linked list
    so basically is node.next.next = node.next
    '''
    temp = Node(-1)

    while (head != None):
        if (head.next == None):
            return None

        if (head.next == temp):
            break

        nex = head.next 
        head.next = temp 
        head = nex 

    return head

def insert_mid(head, x):
    '''
    Give the ability to insert 
    in the middle of a linked list

    '''
    if(head == None):
        head = Node(x)
    else:
        #search for middle of linked list
        newNode = Node(x)
  
        curr = head
        length = 0
        while(curr != None):
            curr = curr.next
            length += 1
        if(length % 2 == 0):
            count = length / 2 
        else:
            (length + 1) / 2
        #insert in middle
        curr = head
        while(count > 1):
            count -= 1
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode

def show(head):
    temp = head
    while temp is not None:
        print(str(temp.data), end= " ")
        temp = temp.next

def remove(head, value):
        """
        Remove the first node that contains 'value'.
        """
        temp = head

        if (temp is not None):
            if temp.data == value:
                head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None
def merge_list(headA, headB):
    '''
    This would merge sort 2 list
    so it would check for lowest 
    first value in both list 
    and put that one in new list
    '''
    dummyNode = Node(0)
    tail = dummyNode
    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
    
        tail = tail.next
    return dummyNode.next


'''
Solution 1: Insert in empty list
input: 6
output: [none]
'''
x = 6
head = None
insert_mid(head, x)
print('Problem 1:')
show(head)
print('\n\n')

'''
Check if my nodes work
'''
linked = Node(1)
linked.next = Node(2)
linked.next.next = Node(3)
linked.next.next.next = Node(4)
linked.next.next.next.next = Node(5)
linked.next.next.next.next.next = Node(6)

'''
Solution 2: Showing a list

input: 1,2,3,4,5,6
Output: 1 2 3 4 5 6 
'''
print('Problem 2:')
show(linked)
print('\n\n')

'''
check if inserting in middle works

Solution 3: inserting in middle of list
list: 1,2,3,4,5,6
input mid: 6
output: 1 2 3 6 4 5 6
'''
print('Problem 3:')
insert_mid(linked, x)
show(linked)
print('\n\n')
'''
Check if remove would work

Solution 4: removing n value
list: 1,2,3,6,4,5,6
remove: 6
output: 1 2 3 4 5 6
'''
print('Problem 4:')
remove(linked, 6)
show(linked)
print()

print('\n\n')
print('Problem 5: ')
# Detect first node in a loop
curr = Node(50)
curr.next = Node(20)
curr.next.next = Node(15)
curr.next.next.next = Node(4)
curr.next.next.next.next = Node(10)
'''
check if it correctly detects the loop 
or not

Solution 5: Doesn't detect a loop
list, Input: 50,20,15,4,10
Output: Loop does not exist
show output: 50 20 15 4 10
'''
find = detect_loop(head)
if (find == None):
        print("Loop does not exist")
else:
    print("Loop starting node is ", find.data)

print()
show(curr)
print()
print()

head = Node(50)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(4)
head.next.next.next.next = Node(10)

# Create a loop for testing
head.next.next.next.next.next = head.next.next

'''
Solution 6: If there's a loop
list, Input: 50,20,15,4,10, loop back to 15
Output: Loop starting node is  15
show output: 50 -1
'''
print('\n\nProblem 6: ')
find2 = detect_loop(head)
if (find2 == None):
        print("Loop does not exist")
else:
    print("Loop starting node is ", find2.data)

print()
show(head)
print()



print("\n\nProblem 7:")
'''
Check if the merger works as intended.
list 1: 1,2,3,4,5,6
list 2: 50, 20,15,4,10

outcome:1 2 3 4 5 6 50 20 15 4 10
parent_list: 1,2,3,4,5,6,50,20,15,4,10
'''
parent_list = merge_list(linked, curr)
show(parent_list)
print('\n\n\n')