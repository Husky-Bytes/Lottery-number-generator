import random

while True:
    char = input("Auto:1, Set seed:2, Auto*5:3, Set seed*5:4, end:5 -> ")
    if char == "1":
        nums = random.sample(range(1,46),6)
        nums.sort()
        print(nums)
    elif char == "2":
        s = float(input("Write a number: "))
        random.seed(random.getstate()[1][1]*s)
        nums = random.sample(range(1,46),6)
        nums.sort()
        print(nums)
    elif char == "3":
        for i in range(5):
            nums = random.sample(range(1,46),6)
            nums.sort()
            print(nums)
    elif char == "4":
        s = float(input("Write a number: "))
        random.seed(random.getstate()[1][1]*s)
        for i in range(5):
            nums = random.sample(range(1,46),6)
            nums.sort()
            print(nums)
    elif char == "5":
        print("Bye!")
        break
    else:
        print("Try again!")
    print('\n')