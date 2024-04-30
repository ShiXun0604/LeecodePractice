from linked_list.linked_list import ListNode



# 24. Swap Nodes in Pairs
def swapPairs(head):
    # 先處理edge case(0項或是1項)
    if not head or not head.next:
        return head

    # 2項以上
    # 處理首兩項
    node = head.next
    temp = head.next.next
    node.next = head
    head.next = temp
    head = node
    node = node.next

    while node.next and node.next.next:
        temp2 = node.next.next
        temp3 = node.next.next.next
        node.next.next.next = node.next
        node.next.next = temp3
        node.next = temp2

        node = node.next.next
    return head


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None)))))))
    list1 = swapPairs(list1)
    list1.print_list()