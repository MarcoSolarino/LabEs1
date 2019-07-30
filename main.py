import ArrayGenerator as gnrt
import Quicksort as qsrt
import Insertionsort as isrt
import sys
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from prettytable import PrettyTable

sys.setrecursionlimit(10000)

N = []
a = 0
while a < 10**4:
    a = a + 100
    N.append(a)

itimes = []
qtimes = []

imatrix = ([], [], [])
qmatrix = ([], [], [])

for j in range(3):
    for i in N:
        print("sorting", i, "elements")

        v1 = gnrt.random_list(i)
        v2 = v1[:]

        istart = timer()
        isrt.insertionsort(v1)
        iend = timer()
        imatrix[j].append(iend - istart)

        qstart = timer()
        qsrt.quicksort(v2, 0, len(v2) - 1)
        qend = timer()
        qmatrix[j].append(qend - qstart)

for i in range(100):
    ivalue = (imatrix[0][i]+imatrix[1][i]+imatrix[2][i])/3
    itimes.append(ivalue)
    qvalue = (qmatrix[0][i]+qmatrix[1][i]+qmatrix[2][i])/3
    qtimes.append(qvalue)

print("Confronto il tempo nel caso peggiore del quicksort")
v1 = gnrt.q_worst_case(2500)
v2 = v1[:]
qwstart = timer()
qsrt.quicksort(v1, 0, len(v1) - 1)
qwend = timer()
qwtime = qwend - qwstart

ibstart = timer()
isrt.insertionsort(v2)
ibend = timer()
ibtime = ibend - ibstart

print("Quicksort = ")
print(qwtime)
print(" Insertion = ")
print(ibtime)

plt.plot(N, itimes)
plt.title("Insertionsort")
plt.show()

plt.title("Quicksort")
plt.plot(N, qtimes)
plt.show()

plt.title("Insertionsort & Quicksort")
plt.plot(N, itimes)
plt.plot(N, qtimes)
plt.show()

table = PrettyTable(['N', 'Insertionsort', 'Quicksort'])
for x in range(0, 100):
    table.add_row([N[x], itimes[x], qtimes[x]])
print(table)
