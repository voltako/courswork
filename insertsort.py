import random
import time
start_time = time.time()
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
arr =[]
for n in  range(0,1010000,100000):
    for a in range(0,100001,1):
        arr.append(random.randint(1,100000))
    b = len(arr)
    insertion_sort(arr)
    print(n)
    print("%s seconds" % (time.time() - start_time))
