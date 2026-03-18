def check_number(input_number):
    if (input_number % 15) == 0 :
        return "legendary number!"
    elif (input_number % 3) == 0 :
        return "Magic number!"
    elif (input_number % 5) == 0 :
        return "Curse number!"
    else :
        return f"this {input_number} is ordinary number"

def end():
    sit = input("Do you want to continuo?(y/n) ")
    if sit.lower() == 'y':
        game = 0
        return game
    elif sit.lower() == 'n':
        game = 1
        return game
    else:
        print(f"your choose was {sit},Please enter y/n ")
        return end()



game = 0

while (game == 0) :
    input_number = int(input("\nPlease enter number : "))
    answer = check_number(input_number)
    print(answer)
    game = end()