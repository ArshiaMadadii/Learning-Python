import random

def start():
    print(
        '''

        Hello, in this game we want play game\n
        in this game we want guess number in range 0 -200\n
        do you think you can find this number?\n

        '''
    )

def finish():
        print(
        f'''
        Congratulating, you are very luck!\n
        you need {count} times to find this number\n
        number was {computer_number}

        '''
    )


def number_is_valid(your_guess):
    if your_guess > 200 or your_guess <0 :
        response = f"Your guess was {your_guess}\nIt's wrong, you should choose number between 0 -200\n"
        return response
    else :
        if your_guess == computer_number :
            return your_guess
        else :
            if your_guess > computer_number:
                response = "You have TOOOO number!"
                return response
            elif your_guess < computer_number :
                response = "You need number!"
                return response

def input_guess():
    (your_guess) = input("you should guess number! :")
    return int(your_guess)



guess_list=[]
guess = 0
count = 0

computer_number = random.randint(1,200)

start()
while(not (guess == computer_number)):
        guess = input_guess()
        guess = number_is_valid(guess)
        print(guess)
        if guess == computer_number :
            finish()
        count += 1
