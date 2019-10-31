import csv
from matplotlib import pyplot as plt
import numpy as np
from math import *
from cycler import cycler
from scipy import optimize

alpha_chain, alpha_cuckoo = [], []
time_chain, time_cuckoo = [], []


def func(x, k, b):
    return k * x + b


with open("./insert/chain.csv", "r") as chainFile:
    chainReader = csv.reader(chainFile)

    for item in chainReader:
        alpha_chain.append(log(float(item[0])))
        time_chain.append(log(float(item[1]) * 10e6, 2))

chainFile.close()

with open("./insert/cuckoo.csv", "r") as cuckooFile:
    cuckooReader = csv.reader(cuckooFile)

    for item in cuckooReader:
        alpha_cuckoo.append(log(float(item[0])))
        time_cuckoo.append(log(float(item[1]) * 10e6, 2))

cuckooFile.close()

plt.gca().set_prop_cycle(cycler('color', ['c', 'm']))

plt.scatter(alpha_chain, time_chain, marker = '^')

plt.scatter(alpha_cuckoo, time_cuckoo, marker = '+')

plt.xlabel('Log(alpha)')
plt.ylabel('Log(t)')
plt.title('Time vs Load Factor')
plt.legend(['Chaining', 'Cuckoo'], loc = 'upper left')

A1, B1 = optimize.curve_fit(func, alpha_chain, time_chain)[0]
x1 = np.arange(-3, 0, 0.01)
y1 = A1 * x1 + B1
plt.plot(x1, y1, "c")

A2, B2 = optimize.curve_fit(func, alpha_cuckoo, time_cuckoo)[0]
x2 = np.arange(-3, 0, 0.01)
y2 = A2 * x2 + B2
plt.plot(x2, y2, "m")

print(A1, B1)
print(A2, B2)

plt.show()
