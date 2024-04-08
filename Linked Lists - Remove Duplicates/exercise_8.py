class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    current = head

    while (current and current.next) is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
