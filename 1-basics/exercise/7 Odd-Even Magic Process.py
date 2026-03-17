def welcome():
    steps = int(input("\nPlease enter N (number of steps): "))
    current_number = int(input("Please enter X (starting number): "))
    return steps, current_number


def process(steps,current_number):
    i = 0
    for i in range(steps):
        current_number = odd_even(current_number)
        i += 1
    return current_number


def odd_even(number):
    if (number % 2) == 0 :
        number = number / 2
    else :
        number = (number * 2) - 1
    return number



steps, current_number = welcome()

output_number = process(steps,current_number)
print(f"output number is : {output_number}")