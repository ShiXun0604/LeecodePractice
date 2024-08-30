from linked_list.linked_list import ListNode



# 61. Rotate List
def rotateRight(head, k):
    # 先計算list項數
    node = head
    len_list = 0
    while node and node.next:
        len_list += 1
        node = node.next
    if head:
        len_list += 1

    # 處理edge case
    if len_list in [0, 1]:
        return head
    else:
        tail = node

    # 處理旋轉
    n = len_list - (k % len_list)
    if n == len_list:
        return head  # 不需要動
    else:
        node = head
        for i in range(n-1):
            node = node.next
        
        # 從中間對半切，尾接頭
        new_head = node.next
        node.next = None
        tail.next = head
        return new_head


if __name__ == '__main__':
    list1 = ListNode(1, None)
    list1 = rotateRight(list1, 10)
    list1.print_list()