import random
import time
f = open('quicksort.txt','w')
start_time = time.time()
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
      if arr[j] <= pivot:
        i = i+1
        arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quickSort(arr, low, high):
    if len(arr) == 1:
      return arr
    if low < high:
      pi = partition(arr, low, high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)


arr =[]
for n in  range(0,1010000,100000):
    for a in range(0,100001,1):
        arr.append(random.randint(1,100000))
    b = len(arr)
    quickSort(arr, 0, b - 1)
    print(n)
    print("%s seconds" % (time.time() - start_time))
    timer = ("%s"(time.time() - start_time))
    f.write(str(n, timer) + '\n')
f.close()


#n = len(arr)
#quickSort(arr, 0, n-1)
#print("%s seconds" % (time.time() - start_time))