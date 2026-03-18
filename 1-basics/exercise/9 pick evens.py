def pick_evens(*args):
    evens = []
    for i in args:
        if i % 2 == 0:
            evens.append(i)
    return evens


numbers = input("Please enter numbers: ").split()

nums = []
for n in numbers:
    nums.append(int(n))

# Input values are strings after using split(), so we convert them to integers.
# We append each converted number to 'nums' to create a list of integers.


pick = pick_evens(*nums)
print(pick)
