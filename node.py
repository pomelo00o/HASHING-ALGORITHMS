from kv import *


class ListNode(object):
    def __init__(self, k, v):
        self.kv = KVPair(k, v)
        self.next = None
