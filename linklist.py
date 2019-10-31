from node import *


class LinkList(object):
    def __init__(self):
        self.head = None

    def search(self, key):
        dummy = ListNode(-1, -1)
        curr = dummy
        curr.next = self.head
        while curr.next:
            if curr.next.kv.key == key:
                return curr.next.kv.val
            else:
                curr = curr.next
        return -1

    def insert(self, key, val):
        dummy = ListNode(-1, -1)
        curr = dummy
        curr.next = self.head
        isExisted = False
        while curr.next:
            if curr.next.kv.key == key:
                curr.next.kv.val = val
                isExisted = True
                break
            else:
                curr = curr.next
        if not isExisted:
            node = ListNode(key, val)
            curr.next = node
        self.head = dummy.next
        return dummy.next

    def remove(self, key):
        dummy = ListNode(-1, -1)
        curr = dummy
        curr.next = self.head
        while curr.next:
            if curr.next.kv.key == key:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        self.head = dummy.next
        return dummy.next

    def prompt(self):
        if self.head is None:
            print("")
            return
        node = self.head
        while node is not None:
            print('(', node.kv.key, ',', node.kv.val, ')')
            node = node.next
