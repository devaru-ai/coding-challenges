# 1. Print All Elements:
# Given the head of a linked list, write code to print every element one at a time from head to tail.

def printAllElements(head):
    result = []
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    return result

# Linked List Drill 2: Find the Length
# Given the head of a linked list, write a function that returns the length (number of nodes) in the list.

def findTheLength(head):
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count

# Linked List Drill 3: Find the Last Element
# Return the value of the last node in a singly linked list (assume the list is non-empty).

def lastElement(head):
    cur = head
    while cur.next is not None:
        cur = cur.next
    return cur

# Linked List Drill 4: Search for Value
# Given a value and the head of a linked list, return True if the value exists in the list, False otherwise.

def searchForValue(head, k):
    cur = head
    while cur is not None:
        if cur.val == k:
            return True
        cur = cur.next
    return False

# Linked List Drill 5: Insert at the End
# Given the head of a singly linked list and a value, insert a new node containing that value at the end of the list.

def insertAtEnd(head, k):
    new_node = ListNode(k)
    if head is None:
        return new_node
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = new_node
    return head

# Drill 6: Delete a Node by Value
# Given the head of a linked list and a value k, delete the first node with value k.
# Edge cases to consider: deleting the head, deleting last node, deleting value not present.

def deleteNode(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev, cur = dummy, head
    while cur:
        if cur.val == k:
            prev.next = cur.next
            break
        prev, cur = cur, cur.next
    return dummy.next

# Drill 7: Reverse a Linked List
# Given the head of a singly linked list, reverse the list in-place and return the new head.
def reverseLinkedList(head):
    prev = None
    cur = head
    while cur:
        temp = cur.next       # Store next node
        cur.next = prev       # Reverse pointer
        prev = cur            # Advance prev
        cur = temp            # Advance cur
    return prev               # prev is the new head

        
# Drill 8: Find the Middle Node
# Return the middle node of the linked list. If the list has an even number of nodes, return the second middle node.
# Hint: Try the fast & slow pointer approach.

def middleNode(head):
    slow, fast = head, head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Drill 9: Detect a Cycle
# Return True if there is a cycle in the linked list (a node points back to a previous node), False otherwise.
def detectCycle(head):
    slow, fast = head, head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Drill 10: Merge Two Sorted Lists
# Given heads of two sorted linked lists, merge them into a single sorted linked list and return the new head.

def mergeSortedLists(list1, list2):
    dummy = ListNode(0)
    cur = dummy
    num1, num2 = list1, list2
    while num1 and num2:
        if num1.val < num2.val:
            cur.next = num1
            num1 = num1.next
        else:
            cur.next = num2
            num2 = num2.next
        cur = cur.next  # advance cur after adding a node

    # Attach remaining nodes if any list is not empty
    if num1:
        cur.next = num1
    if num2:
        cur.next = num2

    return dummy.next

    

        