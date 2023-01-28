#Question 4

class List_node:
    def __init__(self, val = 0, nextNode=None):
        self.val = val
        self.next = nextNode


def print_list(node: List_node):
    while node is not None:
        print(str(node.val), end=" ")
        node = node.next
    print()


def merge_lists(l1: List_node, l2: List_node) -> List_node:
    # Check if either of the lists is null
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        temp = head = List_node(l1.val)
        l1 = l1.next
    else:
        temp = head = List_node(l2.val)
        l2 = l2.next

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp.next = List_node(l1.val)
            l1 = l1.next
        else:
            temp.next = List_node(l2.val)
            l2 = l2.next
        temp = temp.next

    while l1 is not None:
        temp.next = List_node(l1.val)
        l1 = l1.next
        temp = temp.next

    while l2 is not None:
        temp.next = List_node(l2.val)
        l2 = l2.next
        temp = temp.next
    return head


if __name__ == '__main__':
    h1 = List_node(1)
    h1.next =List_node (2)
    h1.next.next = List_node(4)
    h2 = List_node(1)
    h2.next =List_node (3)
    h2.next.next = List_node(4)
    print_list(merge_lists(h1, h2))