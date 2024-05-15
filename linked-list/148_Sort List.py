from linked_list.linked_list import ListNode



class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        return self.mergeTwoLists(l, r)
    
    def mergeTwoLists(self, list1, list2):
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
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # 有一邊沒資料了，直接串上另一邊資料
        if list1:
            node.next = list1
        else:
            node.next = list2

        return head


head = ListNode(1, ListNode(2, ListNode(4, ListNode(3))))
ans = Solution().sortList(head)
print(ans.print_list())