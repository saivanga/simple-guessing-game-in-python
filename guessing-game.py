from random import randint

answer = input(
    "This is a game where you guess a number between 1 and 100. If you guess correctly, you win. What is a number between 1 and 100: "
)

real_num = randint(1, 100)
print(real_num)

if int(answer) == real_num:
    print("Congratulations! You Won!")

while int(answer) < real_num and int(answer) != real_num:
    print("That was too low!")
    input("What is a number between " + str(answer) + " and 100: ")


while int(answer) > real_num and int(answer) != real_num:
    print("That was too high!")
    input("What is a number between 1 and " + str(answer) + ": ")

