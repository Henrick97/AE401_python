import random
num = random.randint(1,20)
user = input()
user = int(user)
x = 0
while x <= 5:
    x = x+1
    if x == 5:
        print('輸了')
    if user < num:
        print("太小")
    elif user > num:
        print('太大')
    elif user == num:
        print('玩了',x,'次')
