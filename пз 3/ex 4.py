import random
n = 0
f = 0
b1 = 0
b2 = 0
o = 0
while f < 3:
    b1 = random.randint(0, 10)
    b2 = random.randint(0, 10)
    o = b1 + b2
    h = int(input(f'{b1} + {b2} ='))
    if o == h:
        print('Правильно!')
        n += 1
    else:
        print('Ответ неверный')
        f += 1
print(f'Игра окончена. Правильных ответов: {n}')