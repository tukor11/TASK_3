import random
main_num, guess_num = random.randint (1, 9), 0
while main_num != guess_num:
    guess_num = int(input("You are to guess a number between 1 and 9 until you get it right : "))
    if guess_num > 9:
        print("wrong guess, try again!")
        continue
        if guess_num < 9:
            print("Well guessed !")
