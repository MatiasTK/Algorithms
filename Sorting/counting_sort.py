import random

MAX_NUMBER = 256


def counting_sort(array):
    length = len(array)

    count = [0] * MAX_NUMBER
    output = [0] * length

    for i in array:
        count[i] += 1

    for i in range(MAX_NUMBER):
        count[i] += count[i - 1]

    for i in range(length):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    return output


random_array = []
for index in range(0, 20):
    random_array.append(random.randint(0, 100))

print("Unsorted array:", random_array)

res = counting_sort(random_array)

print("Sorted array:", res)
