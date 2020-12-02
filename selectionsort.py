import random
import time
f = open('selectionsort.txt','w')
start_time = time.time()
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
arr =[]
for n in  range(0,1010000,100000):
    for a in range(0,100001,1):
        arr.append(random.randint(1,100000))
    b = len(arr)
    selection_sort(arr)
    print(n)
    timer = (time.time() - start_time)
    print(timer)
    print((timer, n), file=f)
f.close()