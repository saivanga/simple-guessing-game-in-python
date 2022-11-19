from random import randint

guess_num = int(input("what is a number between 1 and 100: "))
real_num = randint(1, 100)
print(real_num)

if guess_num == real_num:
    print("Congrats! You Won!")

while guess_num < real_num:
    print("Too Low")
    input("What is a number between "  + str(guess_num) +  " and 100: ")

while guess_num > real_num:
    print("Too High")
    input("What is a number between 1 and " + str(guess_num) + ": ")