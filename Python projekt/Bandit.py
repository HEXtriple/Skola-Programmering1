import random as rand; import turtle

SYMBOLS = ["💛", "💥", "❌", "⚜", "🟢", "💲"]
NUMBER_OF_SYMBOLS = 5

print("\n"*5, "Welcome to the slot marchine!", end="|")
for i in SYMBOLS:
    print(i, end="|")
print("\n")

# Level 1:  Extend this program so that it generates a list of symbols, prints the symbols and then calculates and prints the winnings.
# Level 2:  Introduce a bank that keeps track of the users winnings. Print the current amount in the bank after each round.
# Level 3:  Let the user bet an amount from the bank each round. Verify that the user is not betting more than what is currently in the bank.
#           Multiply the winnings by the bet.


def play():
    playing = True
    while (playing):
        random_symbols = generate_random_symbols()
        print_symbols(random_symbols)
        playing = play_again()

def end():
    import turtle
    turtle.write("Thanks for playing")
    turtle.hideturtle()
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.speed(1000)
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()



def play_again():
    play_again_user_input = input("Play again? (y/n) -> ")
    play_again_bool = (play_again_user_input == "y" or play_again_user_input == "Y")
    return play_again_bool


def generate_random_symbols():

    return [rand.choice(SYMBOLS)]


def calculate_winnings(list_of_symbols):
    '''
    This function takes a list of symbols and how much that list of symbols is worth.
    Implement rules of your choice here.
    Example:
      one 💲 => 1
      two of a kind => 2
      three of a kind => 10
      four of a kind => 100
      five of a kind => Jackpot
    '''


def print_symbols(list_of_symbols):
    print(f"""                              .-------.
                              |Jackpot|
                  ____________|_______|____________
                 |  __    __    ___  _____   __    |  
                 | / _\  / /   /___\/__   \ / _\   | 
                 | \ \  / /   //  //  / /\ \\ \  25|  
                 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
                 | \__/\____/\___/   \/     \__/ []|
                 |===_______===_______===_______===|
                 ||*|\_     |*| _____ |*|\_     |*||
                 ||*|| \ _  |*||     ||*|| \ _  |*||
                 ||*|     {list_of_symbols}     |*||
                 ||*| (_)   |*||_____||*| (_)   |*|| __
                 ||*|_______|*|_______|*|_______|*||(__)
                 |===_______===_______===_______===| ||
                 ||*| _____ |*|\_     |*|  ___  |*|| ||
                 ||*||     ||*|| \ _  |*| |_  | |*|| ||
                 ||*||*BAR*||*| \_(_) |*|  / /  |*|| ||
                 ||*||_____||*| (_)   |*| /_/   |*|| ||
                 ||*|_______|*|_______|*|_______|*||_//
                 |===_______===_______===_______===|_/
                 ||*|  ___  |*|   |   |*| _____ |*||
                 ||*| |_  | |*|  / \  |*||     ||*||
                 ||*|  / /  |*| /_ _\ |*||*BAR*||*||              
                 ||*| /_/   |*|   O   |*||_____||*||        
                 ||*|_______|*|_______|*|_______|*||
                 |lc=___________________________===|
                 |  /___________________________\  |
                 |   |                         |   |
                _|    \_______________________/    |_
               (_____________________________________)""")


play()  
end()