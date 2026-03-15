shop = {
    "banana"    : 20 ,
    "watermelon" : 10 ,
    "apple" : 5 ,
    "strawberry" : 15 ,
    "cucumber" : 2 ,
    "cherry" : 5 ,
    }

def welcome():

    message = "Hi welcome, I'm your assistant do you want some :\nbanana, watermelon, apple, strawberry, cucumber or cherry ?"
    print(message)

def your_order():
    order = input("this is my order list:")
    return order

def add_order(your_order):

    order_list = []
    least = 0
    count = 0

    for i in your_order:
        if i == " " :
            new_order = your_order[least:count]
            order_list.append(new_order)
            count +=1
            least  = count
        elif i == your_order[-1] :
            count +=1
            new_order = your_order[least:count]
            order_list.append(new_order)
        else :
            count +=1

    order_list = order_is_TRUE(order_list)
    return order_list

def order_is_TRUE(order_list):

    correct_order_list   = []
    guess_order_list     = []
    #incorrect_order_list = []

    for order0 in order_list:
        for key in shop.keys():
            if key == order0:
                correct_order_list.append(key)
            elif key.lower() == order0.lower() :
                guess_order_list.append(key)

    for order1 in guess_order_list:
        answer = input(f"Do you want a {order1}? y/n ")
        if answer.lower() == "y":
            correct_order_list.append(order1)
            print("we add it in the list!")

    return correct_order_list


def calculate_order(correct_order_list):
    lent = len(correct_order_list)
    cost = 0
    for i in range(lent):
        cost += shop[correct_order_list[i]]
    return cost

def sale (cost):
    if cost >=30 and cost <50 :
        cost = cost* 0.90
        return f"you have 10% discount, your cost is {cost}$"
    elif cost >= 50 :
        cost = cost* 0.85
        return f"you have 15% discount, your cost is {cost}$"
    else :
        return f"your cost is {cost}$"




welcome()
your_order = your_order()
order_list = add_order(your_order)
price = calculate_order(order_list)
cost = sale(price)
print(cost)