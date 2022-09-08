import random


def linear_search(list_of_numbers, number_to_search):
    pos = -1

    for index, number in enumerate(list_of_numbers):
        if number == number_to_search:
            pos = index

    return pos


numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))

print("List of numbers: ", numbers)
to_search = int(input("Enter a number to search: "))

ans = linear_search(numbers, to_search)

if ans == -1:
    print("Number not found")
else:
    print("Number found at position: ", ans)
