def loop_size(node):
    slow = node
    fast = node

    while (fast and fast.next) is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    length = 0
    fast = fast.next

    while slow != fast:
        length += 1
        fast = fast.next

    return length + 1
