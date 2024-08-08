import random


def play():

    while True:
        user = input("What's your choice ? 'r' for Rock,'p' for Paper,"
                     "'s' for Scissor or 'q' to quit: \n")
        if user == 'q':
            print("Thanks for playing!! Goodbye")
            break

        if user not in ['r', 'p', 's']:
            print("Invalid choice, plaese try again")  
            continue
        
        computer = random.choice(['r', 'p', 's'])
        
        if user == computer:
            print("computer choice is: ", computer)
            print("It's a Tie.")
        
        if is_win(user, computer):  # if True win and Computer loose.
            print("computer choice is: ", computer)
            print("You Won!!!")
        
        if is_win(computer, user):  # Computer win and you loose.
            print("computer choice is: ", computer)
            print("YOu Lost!!!")


# r > s, s > p, p> r
def is_win(player, apponent):
    if (player == 'r' and apponent == 's') or (player == 's' and apponent == 'p') or (player == 'p' and apponent == 'r'):
        return True


print(play())