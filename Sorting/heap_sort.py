import random


def heapify(array, length):
    start = (length - 2) // 2  # Parent(length-1)
    while start >= 0:
        sift_down(array, start, length - 1)
        start -= 1

    print(array)


def sift_down(array, start, end):
    root = start
    left_child = 2 * root + 1  # LeftChild(root)

    while left_child <= end:
        child = 2 * root + 1
        swap = root

        if array[swap] < array[child]:
            swap = child
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap == root:
            return

        array[root], array[swap] = array[swap], array[root]
        root = swap
        left_child = 2 * root + 1  # LeftChild(root)


def heap_sort(array):
    length = len(array)
    end = length - 1

    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        sift_down(array, 0, end)


random_array = []
for index in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

heap_sort(random_array)

print("Sorted array:", random_array)
