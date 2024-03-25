import random
def a():
    a = []
    for i in range(5):
        n = random.randint(0, 10)
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
def b():
    a = []
    for i in range(5):
        n = random.randint(0, 10)
        a.append(n)
    for i in range(5):
        c = a.count(a[i])
        if c >= 2:
            print(a)
            print(a[i])
            break
def c():
    data = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    t = tuple(data)
    a = int(input("Сколько выходных дней Вы хотите? "))
    if a == 0:
        print(f"Ваши рабочие дни: {t}")
    elif a == 1:
        print(f"Ваши рабочие дни: {t[:6]}")
        print(f"Ваши не рабочие дни: {t[6:]}")
    elif a == 2:
        print(f"Ваши рабочие дни: {t[:5]}")
        print(f"Ваши не рабочие дни: {t[5:]}")
    elif a == 3:
        print(f"Ваши рабочие дни: {t[:4]}")
        print(f"Ваши не рабочие дни: {t[4:]}")
def d():
    a = ["Чыпсымаа", "Керган", "Воронков", "Ключников", "Иванов", "Торхов", "Тянутова", "Михалев", "Уланова",
         "Головченко"]
    b = ["Петров", "Петрова", "Аликина", "Белкина", "Ольховик", "Кучинова", "Козодёрова", "Близгарев", "Семенов",
         "Федоров"]
    c = []
    for i in range(5):
        n = random.randint(0, 9)
        if c.count(a[n]) == 0:
            c.append(a[n])
        else:
            n = random.randint(0, 9)
            c.append(a[n])
    for i in range(5):
        n = random.randint(0, 9)
        if c.count(b[n]) == 0:
            c.append(b[n])
        else:
            n = random.randint(0, 9)
            c.append(b[n])
    t = tuple(c)
    print(a)
    print(b)
    print(t)
    print(len(t))
    t = sorted(t)
    print(t)
    if t.count("Иванов") > 0:
        print(t.count("Иванов"))
    else:
        print("Фамилия Иванов не входит")
