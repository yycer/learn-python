import random

# 添加随机数
count = 3
ans = random.randint(1, 10)

while count > 0:
    num = input("Please enter a number: ")
    guess = int(num)

    if guess == ans:
        print("Bingo!")
        break
    else:
        if guess < ans:
            print("The input number is less than the answer.")
        else:
            print("The input number is greater than the answer.")
    count = count - 1

print("Game over")
