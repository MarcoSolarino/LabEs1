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
max_elements = 10**3
passo = 5
iterazioni = 10

while a < max_elements:
    a = a + passo
    N.append(a)

itimes = []
qtimes = []


for j in range(iterazioni):
    print("iterazione ", j+1)
    i_current_tomes = []
    q_current_times = []

    for i in N:
        vi = gnrt.random_list(i)
        vq = vi[:]
        init = timer()
        isrt.insertionsort(vi)
        i_current_tomes.append(timer() - init)

        init = timer()
        qsrt.quicksort(vq, 0, (len(vq) - 1))
        q_current_times.append(timer() - init)

    itimes.append(i_current_tomes)
    qtimes.append(q_current_times)

i_average = []
q_average = []

length_vectors = int(max_elements / passo)

for i in range(length_vectors):
    pi = 0
    pq = 0
    for j in range(iterazioni):
        pi += itimes[j][i]
        pq += qtimes[j][i]
    i_average.append(pi/iterazioni)
    q_average.append(pq/iterazioni)


plt.plot(N, i_average)
plt.title("Insertionsort")
plt.show()

plt.title("Quicksort")
plt.plot(N, q_average)
plt.show()

plt.title("Insertionsort & Quicksort")
plt.plot(N, i_average, label="insertionsort")
plt.plot(N, q_average, label="quicksort")
plt.legend()
plt.show()

table = PrettyTable(['N', 'Insertionsort', 'Quicksort'])
for x in range(length_vectors):
    table.add_row([N[x], i_average[x], q_average[x]])
print(table)
