input = input("please write somethings : ")

input = input.lower()

print(input)

string = []
count = 0
least = 0

for i in input:
    #name =""
    if i == ' ':
        word = input[least:count]
        string.append(word)
        count += 1
        least = count
    elif i == input[-1] :
        count += 1
        word = input[least:count]
        string.append(word)
    else :
        count += 1

print(string)