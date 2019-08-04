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

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a



def MergeSort(A):
    i = 0
    C = []
    while i < (len(A) // 2):
        C.append(A[i])
        i += 1
    D = []
    while i < (len(A)):
        D.append(A[i])
        i += 1
    D = MergeSort(A[:len(A)//2])
    #C = MergeSort(A)
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


    print(k)
    print(A)



MergeSort(A)