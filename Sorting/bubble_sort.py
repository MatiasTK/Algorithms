from operator import le
import random


def bubble_sort(array):
    length = len(array)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux


random_array = []
for i in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

bubble_sort(random_array)

print("Sorted array:", random_array)
