def stringify(node):
    total = []
    current = node
    while current is not None:
        total.append(str(current.data) + " -> ")
        current = current.next
    total.append("None")
    return "".join(total)
