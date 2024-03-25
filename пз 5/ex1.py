import random
a = []
for i in range(5):
    n = random.randint(0,10)
    a.append(n)
y = int(input("Введите число от 0 до 10: "))
h = False
for i in range(5):
    if a[i] == y:
        print(a)
        print(y)
        print("Вы угадали число!")
        h = True
        break
if h == False:
    print(a)
    print(y)
    print("Вы не угадали число!")