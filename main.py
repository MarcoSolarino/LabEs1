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

for i in N:
    print("sorting", i, "elements")

    if i == 2500:
        v1 = gnrt.random_list(i)
        v2 = gnrt.q_worst_case(i)  # caso peggiore quicksort

    elif i == 5000:
        v1 = gnrt.q_worst_case(i)  # caso migliore insertionsort
        v2 = gnrt.random_list(i)

    elif i == 8000:
        v1 = gnrt.i_worst_case(i)  # caso peggiore insertionsort
        v2 = gnrt.random_list(i)

    else:
        v1 = gnrt.random_list(i)
        v2 = v1[:]

    istart = timer()
    isrt.insertionsort(v1)
    iend = timer()
    itimes.append(iend - istart)

    qstart = timer()
    qsrt.quicksort(v2, 0, len(v2) - 1)
    qend = timer()
    qtimes.append(qend - qstart)

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
