

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    current = llist

    while current:
        current.prev, current.next = current.next, current.prev

        if current.prev is None:
            return current

        current = current.prev    # Write your code heredef reverse(llist):

