import random


def create(n):
    A = []
    for j in range(n):
        A.append(j)
    return A


def random_list(n):
    A = create(n)
    random.shuffle(A)
    return A


def q_worst_case(n):
    return create(n)


def i_worst_case(n):
    A = create(n)
    for i in range(n//2):
        tmp = A[i]
        A[i] = A[n-i-1]
        A[n-i-1] = tmp
    return A

