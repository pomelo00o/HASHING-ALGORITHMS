from linklist import *


class Chaining(object):
    def __init__(self):
        self.N = 373
        self.alpha = 0
        self.cnt = 0
        self.table = [LinkList() for i in range(self.N)]

    def hash(self, key):
        return key % self.N

    def search(self, key):
        k = self.hash(key)
        return self.table[k].search(key)

    def insert(self, key, val):
        k = self.hash(key)
        isExisted = (self.table[k].search(key) != -1)
        self.table[k].insert(key, val)
        if not isExisted:
            self.cnt += 1
            self.alpha = self.cnt / self.N
            if self.alpha >= 1:
                self.N *= 2
                self.rehash()

    def remove(self, key):
        k = self.hash(key)
        isExisted = (self.table[k].search(key) != -1)
        self.table[k].remove(key)
        if not isExisted:
            self.cnt -= 1
            self.alpha = self.cnt / self.N
            if self.alpha <= 0.25:
                self.N /= 2
                self.rehash()

    def rehash(self):
        all = []
        self.cnt = 0
        for lst in self.table:
            head = lst.head
            while head:
                kv = head.kv
                all.append(kv)
                head = head.next
        self.table = [LinkList() for i in range(0, self.N)]
        for kv in all:
            self.insert(kv.key, kv.val)

    def prompt(self):
        for i in range(0, self.N):
            print(i, ':')
            self.table[i].prompt()
