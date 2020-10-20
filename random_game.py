import random

game_num = random.randint(0, 1)

while True:
    guess_num = int(input('请输入一个数字'))
    if guess_num == game_num:
        print('你猜对了')
        break
    else:
        print('你猜错了请重新输入')
