import math
import time
import random
f = open('introsort.txt','w')
start_time = time.time()
def introSort(arr,d):
    n = len(arr)
    if n <= 1:
        return
    elif d == 0:
        heapSort(arr)
    else:
        p = partition(arr)
        arr1 = arr[:p]
        arr2 = arr[p+1:n]
        introSort(arr1, d-1)
        introSort(arr2, d-1)
        for i in range(0, len(arr1)):
            arr.insert(i, arr1[i])
            arr.pop(i+1)
        for i in range(0, len(arr2)-1):
            arr.insert(i+p+1, arr2[i])
            arr.pop(i+p+2)

def heapSort (arr):
    END = len(arr)
    for k in range ( int(math.floor(END/2)) - 1, -1, -1):
        heapify(arr, END, k)

    for k in range(END, 1, -1):
        swap(arr, 0, k-1)
        heapify(arr, k-1, 0)

def partition(arr):
    hi = len(arr)-1
    x = arr[hi]
    i = 0
    for j in range(0, hi-1):
        if arr[j] <= x:
            swap(arr, i, j)
            i = i + 1
    swap(arr, i, hi)
    return i

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heapify(arr,iEnd,iRoot):
    iL = 2*iRoot + 1
    iR = 2*iRoot + 2
    if iR < iEnd:
        if (arr[iRoot] >= arr[iL] and arr[iRoot] >= arr[iR]):
            return

        else:
            if(arr[iL] > arr[iR]):
                j = iL
            else:
                j = iR
            swap(arr, iRoot, j)
            heapify(arr, iEnd, j)
    elif iL < iEnd:
        if (arr[iRoot] >= arr[iL]):
            return
        else:
            swap(arr, iRoot, iL)
            heapify(arr,iEnd,iL)

    else:
        return
arr =[]
for n in  range(0,1010000,100000):
    for a in range(0,100001,1):
        arr.append(random.randint(1,10000))
    b = len(arr)
    introSort(arr, 2)
    print(n)
    timer = (time.time() - start_time)
    print(timer)
    print((timer,n),file=f)
f.close()

