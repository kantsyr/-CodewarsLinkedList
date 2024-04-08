def swap_pairs(head):
    if (head and head.next) is None:
        return head

    current = head
    next_n = head.next

    current.next = swap_pairs(next_n.next)
    next_n.next = current

    return next_n
