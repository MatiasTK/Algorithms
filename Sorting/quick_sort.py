import random


def quicksort_lomuto(array, start, end):
    if start >= end or start < 0:
        return

    pivot = partition_lomuto(array, start, end)

    quicksort_lomuto(array, start, pivot - 1)
    quicksort_lomuto(array, pivot + 1, end)


def partition_lomuto(array, start, end):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap

    i += 1
    array[i], array[end] = array[end], array[i]  # Swap
    return i


# --------------------------------------------------------------------------------------------------


def quicksort_hoare(array, start, end):
    if start < end:
        pivot = partition_hoare(array, start, end)
        quicksort_hoare(array, start, pivot)
        quicksort_hoare(array, pivot + 1, end)


def partition_hoare(array, start, end):
    pivot = array[start]  # Floor division
    i = start - 1
    j = end + 1

    while True:

        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


random_array = []
for index in range(0, 10):
    random_array.append(random.randint(0, 100))

random_array_copy = random_array.copy()

print("Unsorted array:", random_array)

quicksort_lomuto(random_array, 0, len(random_array) - 1)
quicksort_hoare(random_array_copy, 0, len(random_array_copy) - 1)

print("Sorted array (lomuto scheme):", random_array)
print("Sorted array (hoare scheme):", random_array_copy)
