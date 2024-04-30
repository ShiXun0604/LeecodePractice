from linked_list.linked_list import ListNode



# 141. Linked List Cycle
def hasCycle(head):
    addr_dict = {}

    node = head
    while node:
        if node in addr_dict.keys():
            return True
        addr_dict[node] = node.val
        node = node.next
    return False


if __name__ == '__main__':
    tail = ListNode(4, None)
    head = ListNode(3, ListNode(2, ListNode(0, tail)))
    tail.next = head.next
    print(hasCycle(head))