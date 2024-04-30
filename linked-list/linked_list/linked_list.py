class ListNode:
    def __init__(self, x=None, next=None):
        self.val = x
        self.next = next

    def print_list(self):
        node = self
        print('[', end='')
        while node.next:
            print(node.val, end=", ")
            node = node.next
        print(node.val, end='')
        print(']')