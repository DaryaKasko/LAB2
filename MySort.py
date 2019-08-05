import random
import datetime
import prettytable
import matplotlib.pyplot as plt

N = int(input(print("Введите количество элементов: \n")))
min = int(input(print("ведите минимальный элемент списка: \n")))
max = int(input(print("ведите максимальный элемент списка: \n")))

A = []

for i in range(N):
    A.append(random.randint(min, max))
print(A)

B = A.copy()
print(B)


"""x = []
for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random()*(max - min)+min)))
"""


def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        C = A[:mid]
        D = A[mid:]
        MergeSort(C)
        MergeSort(D)
        i = 0
        j = 0
        k = 0
        while i < len(C) and j < len(D):
                if C[i] < D[j]:
                    A[k] = C[i]
                    i += 1
                else:
                    A[k] = D[j]
                    j += 1
                k = k + 1
        while i < len(C):
            A[k] = C[i]
            i += 1
            k += 1
        while j < len(D):
            A[k] = D[j]
            j += 1
            k += 1

def SelectSort(A):
    for i in range(len(A) - 1):
        j = i + 1
        min_ind = i
        while j < len(A):
            if A[j] < A[min_ind]:
                min_ind = j
            j += 1
        A[i], A[min_ind] = A[min_ind], A[i]

SelectSort(A)
print(A)

def InsertSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while (j >= 0) and (A[j] > key):
            A[j+1] = A[j]
            j -= 1
            print(j)
        A[j+1] = key


D = [11, 2, 14, 1, 9]
print("D = ", D)
InsertSort(D)
print(D)