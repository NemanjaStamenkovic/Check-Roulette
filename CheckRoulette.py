import random


print("Welcome to Check Roulette. Enter Names to See who will pay the bill today.")
namesString = input("Enter Your Names: ")
names = namesString.split(", ")

namesLen = len(names)

randomNum = random.randint(0, (namesLen - 1))

randomName = names[randomNum]
print(f"{randomName} is going to buy the meal today.")
