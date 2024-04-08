class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    total = list(map(int, s.split(" -> ")[:-1]))
    nodes = [Node(i) for i in total]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0] if nodes else None # head to linked list
