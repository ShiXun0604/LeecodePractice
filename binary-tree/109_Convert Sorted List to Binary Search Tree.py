from lib.binary_search_tree import TreeNode
from lib.linked_list import ListNode



class Solution:
    def __helper(self, head:ListNode, tail:ListNode) -> TreeNode:
        if head == tail:
            return TreeNode(head.val)
        elif head.next == tail:
            return TreeNode(tail.val, TreeNode(head.val))
        else:
            fast, slow = head, head
            prev = head
            while fast != tail and fast.next != tail:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            return TreeNode(
                val = slow.val,
                left = self.__helper(head, prev),
                right = self.__helper(slow.next, tail)
            )

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # edge case:
        if not head:
            return None
        # Find tail
        tail = head
        while tail.next:
            tail = tail.next
        return self.__helper(head, tail)


head = ListNode(1, ListNode(2, ListNode(5, ListNode(7, ListNode(9)))))
ans = Solution().sortedListToBST(head)