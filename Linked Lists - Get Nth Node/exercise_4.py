class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    # Your code goes here.
    if not node:
        raise Exception("Node is empty")
    if index < 0 and not index.isdigit():
        raise Exception("Index must be positive")

    count_0 = 0
    current_0 = node
    while current_0 is not None:
        current_0 = current_0.next
        count_0 += 1
    if count_0 - 1 < index:
        raise Exception("The index must be within the array")

    count = 0
    current = node
    while count < index:
        current = current.next
        count += 1
    return current
  