class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    if head is None:
        return None

    def recursive(current, previous):
        if current is None:
            return previous
        next_n = current.next
        current.next = previous
        return recursive(next_n, current)

    return recursive(head, None)
