import math
import random


def binary_search(list_of_numbers, number_to_search):
    start = 0
    end = len(list_of_numbers) - 1

    while start <= end:
        middle = math.floor((start + end) / 2)  # La mitad del array
        if list_of_numbers[middle] < number_to_search:
            # Si el numero de la mitad es mas chico que el que busco entonces voy a analizar desde la mitad + 1 hasta el final del array.
            start = middle + 1
        elif list_of_numbers[middle] > number_to_search:
            # Si el numero de la mitad es mas grande entonces voy a analizar desde el principio hasta la mitad - 1 del array.
            end = middle - 1
        else:
            return middle

    return -1


def binary_search_recursive(list_of_numbers, number_to_search, start, end):
    if start > end:
        return -1

    middle = math.floor((start + end) / 2)
    if list_of_numbers[middle] < number_to_search:
        return binary_search_recursive(
            list_of_numbers, number_to_search, middle + 1, end
        )
    elif list_of_numbers[middle] > number_to_search:
        return binary_search_recursive(
            list_of_numbers, number_to_search, start, middle - 1
        )
    else:
        return middle


numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
numbers.sort()

print("List of numbers: ", numbers)
to_search = int(input("Enter a number to search: "))

ans = binary_search(numbers, to_search)

if ans == -1:
    print("Number not found")
else:
    print("Number found at position: ", ans)

print("Now doing it with recursion method")
ans = binary_search_recursive(numbers, to_search, 0, len(numbers) - 1)
if ans == -1:
    print("Number not found")
else:
    print("Number found at position: ", ans)
