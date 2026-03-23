def input_numbers(n):
    arr = []
    for i in range(n):
        num = int(input("Enter number: "))
        arr.append(num)
    return arr


def convert(arr):
    rev = []
    for i in range(len(arr)-1, -1, -1):
        rev.append(arr[i])
    return rev


def print_numbers(arr):
    print(arr)


# main
count = int(input("How many numbers? "))

numbers = input_numbers(count)
reversed_numbers = convert(numbers)
print_numbers(reversed_numbers)
