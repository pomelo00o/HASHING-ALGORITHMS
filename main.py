from chaining import *
from cuckoo import *
from random import *

# 'chain' or 'cuckoo'
hashmap = "chain"


class Command(object):
    def __init__(self, action, key, val):
        self.action = action
        self.key = key
        self.val = val


to_insert = Command('i', floor(random() * 100), floor(random() * 100))


def generate_testcase(n):
    filename = './testcase/insert/' + hashmap + '/test_' + str(n) + '.csv'
    for i in range(0, n):
        c = Command('i', floor(random() * 100), floor(random() * 100))
        with open(filename, 'a') as f:
            line = c.action + ',' + str(c.key) + ',' + str(c.val)
            f.write(line)
            f.write('\n')
            f.close()


if __name__ == '__main__':
    outfile = './output/insert/' + hashmap + '.csv'
    N = 373
    if hashmap == 'cuckoo':
        N *= 2
    alpha = 0.05
    while alpha < 1:
        n = floor(alpha * N)
        if n == 0:
            alpha += 0.05
            continue
        # generate_testcase(n)
        filename = './testcase/insert/' + hashmap + '/test_' + str(n) + '.csv'
        c = Chaining()
        with open(filename, 'r') as f:
            lines = f.readlines()
        f.close()
        for i in range(0, len(lines)):
            line = lines[i]
            info = line.split(',')
            key = int(info[1])
            val = int(info[2])
            if info[0] == 'i':
                c.insert(key, val)
            elif info[0] == 's':
                c.search(key)
            elif info[0] == 'r':
                c.remove(key)
        c.insert(to_insert.key, to_insert.val)
        line = str(alpha) + ',' + str(c.n_encountered)
        with open(outfile, 'a') as f:
            f.write(line)
            f.write('\n')
            f.close()
        alpha += 0.05
