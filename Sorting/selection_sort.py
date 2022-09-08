import random


def selection_sort(array):
    length = len(array)

    for i in range(length):
        minium = i
        for j in range(i + 1, length):
            if array[j] < array[minium]:
                minium = j

        if minium != i:
            aux = array[i]
            array[i] = array[minium]
            array[minium] = aux


random_array = []
for index in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

selection_sort(random_array)

print("Sorted array:", random_array)
