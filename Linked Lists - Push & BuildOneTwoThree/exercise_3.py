class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new = Node(data)
    new.next = head
    return new


def build_one_two_three():
    n = None
    n = push(n, 3)
    n = push(n, 2)
    n = push(n, 1)
    return n
