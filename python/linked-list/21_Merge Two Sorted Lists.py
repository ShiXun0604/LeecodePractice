from linked_list.linked_list import ListNode

# 21. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    # 處理list為空時的edge case
    if not list1:
        return list2
    if not list2:
        return list1
    
    # 創建linked list的頭
    if list1.val < list2.val:
        head = ListNode(list1.val)
        list1 = list1.next
    else:
        head = ListNode(list2.val)
        list2 = list2.next

    # 處理兩邊都還有資料的情況
    node = head
    while list1 and list2:
        if list1.val < list2.val:
            node.next = ListNode(list1.val)
            list1 = list1.next
        else:
            node.next = ListNode(list2.val)
            list2 = list2.next
        node = node.next

    # 有一邊沒資料了，直接串上另一邊資料
    if list1:
        node.next = list1
    else:
        node.next = list2

    return head


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(4, None)))


    # index count of arrays
    reslut = mergeTwoLists(list1, list2)
    reslut.print_list()