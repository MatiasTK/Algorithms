import random


def insertion_sort(array):
    length = len(array)

    for i in range(1, length):
        aux = array[i]
        j = i - 1

        while j >= 0 and array[j] > aux:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = aux


random_array = []
for index in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

insertion_sort(random_array)

print("Sorted array:", random_array)
