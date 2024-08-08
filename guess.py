import random

def guess(nums):
    random_number = random.randint(1, nums)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the random number between {nums}: "))
        if guess > random_number:
            print("sorry guess is too high, guess again: ")
        elif guess < random_number:
            print("Sorry guess is too low, Guess again: ")

    print("yayy...Congrats, You have guessed correct Number!!!")  

def computer_guess(nums):
    low = 1
    high = nums
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # or can be high because low and high are same.    
        feedback = input(f"Is {guess} is Too High (H), too Low (L), or Correct (c) :").lower()
        if feedback == 'h':
            high = guess-1  # reassign high to number 1 less than high
        elif feedback == 'l':
            low = guess+1  # reassign low to number 1 morw than high.

    print(f"Yay!!, Computer guessed your number, {guess} ,correctly.")       


computer_guess(100)
