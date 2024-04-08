class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if source is None:
        raise Exception("Source is empty")

    first_node = source
    source = source.next
    first_node.next = dest
    dest = first_node

    return Context(source, dest)
