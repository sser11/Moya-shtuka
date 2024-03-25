import random
a = []
for i in range(5):
    n = random.randint(0,10)
    a.append(n)
for i in range(5):
    c = a.count(a[i])
    if c >= 2:
        print(a)
        print(a[i])
        break