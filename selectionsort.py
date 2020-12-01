import random
import time
start_time = time.time()
def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
arr =[]
for n in  range(0,1010000,100000):
    for a in range(0,100001,1):
        arr.append(random.randint(1,100000))
    b = len(arr)
    selection_sort(arr)
    print("%s seconds" % (time.time() - start_time))
    print(n)