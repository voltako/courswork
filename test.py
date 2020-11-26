# -*- coding: utf-8 -*-
import random
def  quick(arr,low,high):
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


n = 0
a = 0
while n < 1000000:
  n = n + 10000
  while a <10000:
    a = a+1
    arr.append(random.randint(1,100000))
    print(arr)
n = len(arr)
quick(arr, 0, n-1)
print("Sorted array is:")
print(max(arr))
