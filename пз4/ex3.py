b = input("Введите дату: ")
def f(a):
    c = int(b[:2])
    n = int(b[3:5])
    m = int(b[8:])
    if c * n == m:
        return 'число счастливое'
    else:
        return 'число не счастливое'
print(f(b))