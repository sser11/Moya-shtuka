import random
a = ["Чыпсымаа", "Керган", "Воронков", "Ключников", "Иванов", "Торхов", "Тянутова", "Михалев", "Уланова", "Головченко"]
b = ["Петров", "Петрова", "Аликина", "Белкина", "Ольховик", "Кучинова", "Козодёрова", "Близгарев", "Семенов", "Федоров"]
c = []
for i in range(5):
    n = random.randint(0,9)
    if c.count(a[n]) == 0:
        c.append(a[n])
    else:
        n = random.randint(0, 9)
        c.append(a[n])
for i in range(5):
    n = random.randint(0,9)
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
