class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # edge case
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        
        node = head
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2
            
        return head


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
ans = Solution().mergeTwoLists(list1, list2)
print(ans)

while ans:
    print(ans.val)
    ans = ans.next