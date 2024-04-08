class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    new_node = Node(data)

    if head is None or head.data >= data:
        new_node.next = head
        return new_node

    current = head

    while current is not None:
        if current.next is None or int(current.next.data) > data:
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next

    return head
