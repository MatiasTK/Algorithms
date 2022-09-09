import random


def merge(left, right):
    res = []

    while left and right:
        if left[0] <= right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)

    while left:
        res.append(left[0])
        left.pop(0)
    while right:
        res.append(right[0])
        right.pop(0)

    return res


def merge_sort(array):
    length = len(array)

    if length <= 1:
        return array

    left = []
    right = []

    for i, number in enumerate(array):
        if i < length / 2:
            left.append(number)
        else:
            right.append(number)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge_sort_alternative(array):
    if len(array) <= 1:
        return

    middle = len(array) // 2  # Floor division

    left = array[:middle]
    right = array[middle:]

    merge_sort_alternative(left)  # Sort first half
    merge_sort_alternative(right)  # Sort second half

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):  # Copy data to left and right
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1

    # Copy left data
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


random_array = []
for index in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

sorted_array = merge_sort(random_array)

print("Sorted array:", sorted_array)
merge_sort_alternative(random_array)
print("Soarted array alternative: ", random_array)
