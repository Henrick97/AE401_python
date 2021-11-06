import random
num = random.randint(1,20)
user = input()
user = int()
x = 0
while user != num:
    x = x+1
    if x == 5:
        print('輸了')
    user = input()
    user = int(user)
    if user < num:
        print("太小")
    elif user > num:
        print('太大')
    elif user == num:
        print('玩了x次')
