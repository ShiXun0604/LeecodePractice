from linked_list.linked_list import ListNode



# 83. Remove Duplicates from Sorted List
def deleteDuplicates(head):
    node = head
    same_pointer = head

    # 處理edge case
    if not node or not node:
        return

    # 遍歷list每個node，下一個沒東西則跳出迴圈
    while node.next:
        front_value = node.val
        node = node.next

        # 如果數值不一樣，pointer往後指
        if front_value != node.val:
            same_pointer.next = node  # 往後指
            same_pointer = node  # 來到目前位置
    # 處理最後可能重複的部分
    same_pointer.next = None



if __name__ == '__main__':
    list1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, None))))))

    deleteDuplicates(list1)
    list1.print_list()