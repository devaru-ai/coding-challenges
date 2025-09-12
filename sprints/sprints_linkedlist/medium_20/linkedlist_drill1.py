'''
1. Remove N-th Node From End
Given the head of a linked list and an integer n, remove the n-th node from the end and return the updated list.
'''

def removeNthNode(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for _ in range(n+1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return dummy.next

'''
2. Partition List
Rearrange the nodes of the linked list so that all nodes less than a given value x come before nodes greater than or equal to x, while preserving the original relative order.
'''
def partitionList(head, x):
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less, greater = less_dummy, greater_dummy
    cur = head
    while cur:
        if cur.val < x:
            less.next = cur
            less = less.next
        else:
            greater.next = cur
            greater = greater.next
        cur = cur.next
    greater.next = None
    less.next = greater_dummy.next
    return less_dummy.next

'''
3. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return the new head. (You must do this by changing links, not just values.)
'''
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    cur = head
    while cur and cur.next:
        temp = cur.next.next
        prev.next = cur.next    # Point previous to second node of pair
        cur.next.next = cur     # Point second node to first node (swap)
        cur.next = temp         # First node now points to next pair

        prev = cur              # Advance prev for next swap
        cur = temp              # Advance cur for next swap
    return dummy.next

'''
4. Odd-Even Linked List
Group all odd-index nodes together followed by even-index nodes, and return the reordered list.
'''
def oddEvenList(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

'''
5. Intersection of Two Linked Lists
Given the heads of two singly linked lists, return the node where they intersect, or None if they do not.
'''
    
def intersection(list1, list2):
    a, b = list1, list2
    while a != b:
        a = a.next if a else list2
        b = b.next if b else list1
    return a  # Will be None if no intersection


'''
6. Linked List Cycle II
Given a linked list that may contain a cycle, return the node where the cycle begins. If there is no cycle, return None.
'''
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # cycle detected
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast    # start of the cycle
    return None
