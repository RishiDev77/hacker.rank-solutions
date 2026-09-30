

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
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

def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)

    # Empty list
    if llist is None:
        return new_node

    # Insert before current head
    if data <= llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    current = llist

    # Find the correct position
    while current.next and current.next.data < data:
        current = current.next

    # Insert new_node after current
    new_node.next = current.next
    new_node.prev = current

    if current.next:
        current.next.prev = new_node

    current.next = new_node

    return llist
