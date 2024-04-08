class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.

    if (head and head.next) is None:
        raise Exception("Splitting a single node list")

    count = 0
    current = head

    while current is not None:
        count += 1
        current = current.next

    first_count = count // 2 if count % 2 == 0 else count // 2 + 1

    first_head = head
    second_head = head.next
    first_current = first_head
    second_current = second_head

    for _ in range(first_count - 1):
        first_current.next = second_current.next
        first_current = first_current.next
        second_current.next = first_current.next
        second_current = second_current.next

    first_current.next = None

    return Context(first_head, second_head)
