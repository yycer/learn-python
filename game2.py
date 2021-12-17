# 增加循环，和提示大小功能

count = 3

while count > 0:
    num = input("Please enter a number: ")
    guess = int(num)

    if guess == 8:
        print("Bingo!")
        break
    else:
        if guess < 8:
            print("The input number is less than the answer.")
        else:
            print("The input number is greater than the answer.")
    count = count - 1

print("Game over")
