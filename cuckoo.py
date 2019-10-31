from math import *
from kv import *


class Cuckoo(object):
    def __init__(self):
        self.N = 373
        self.alpha = 0
        self.limit = 300
        self.pos = [nan for i in range(0, 2)]
        self.table = [[KVPair(nan, nan) for i in range(0, self.N)], [KVPair(nan, nan) for j in range(0, self.N)]]

    def hash(self, func, key):
        if func == 1:
            return key % self.N
        elif func == 2:
            return floor(key / self.N) % self.N

    def search(self, key):
        for i in range(0, 2):
            k = self.hash(i + 1, key)
            if self.table[i][k].key == key:
                return self.table[i][k].val

    def helper(self, key, val, table_id, cnt):
        if cnt == self.limit:
            self.N *= 2
            self.rehash()
        for i in range(0, 2):
            self.pos[i] = self.hash(i + 1, key)
            if self.table[i][self.pos[i]].key == key:
                self.table[i][self.pos[i]].val = val
                return
        if self.table[table_id][self.pos[table_id]].key is not nan and self.table[table_id][self.pos[table_id]].val is not nan:
            kv = self.table[table_id][self.pos[table_id]]
            self.table[table_id][self.pos[table_id]] = KVPair(key, val)
            self.helper(kv.key, kv.val, (table_id + 1) % 2, cnt + 1)
        else:
            self.table[table_id][self.pos[table_id]] = KVPair(key, val)

    def insert(self, key, val):
        self.helper(key, val, 0, 0)

    def remove(self, key):
        for i in range(0, 2):
            k = self.hash(i + 1, key)
            if self.table[i][k].key == key:
                self.table[i][k] = KVPair(nan, nan)

    def rehash(self):
        all = []
        for i in range(0, 2):
            for kv in self.table[i]:
                if kv.key is not nan and kv.val is not nan:
                    all.append(kv)
        self.table = [[KVPair(nan, nan) for i in range(0, self.N)], [KVPair(nan, nan) for i in range(0, self.N)]]
        for kv in all:
            self.insert(kv.key, kv.val)

    def prompt(self):
        tab1 = 'Table One'
        tab2 = 'Table Two'
        print('%-20s%-20s' % (tab1, tab2))
        for i in range(0, self.N):
            kv1 = self.table[0][i]
            kv2 = self.table[1][i]
            str1 = '(' + str(kv1.key) + ',' + str(kv1.val) + ')'
            str2 = '(' + str(kv2.key) + ',' + str(kv2.val) + ')'
            print('%-20s%-20s' % (str1, str2))
