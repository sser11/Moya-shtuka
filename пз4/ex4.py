b = input("Введите номер билета: ")
def f(a):
    m1 = 0
    m2 = 0
    v = 0
    for i in range(len(b) // 2):
        m1 += int(b[i])
        v = len(b) // 2 + i
        m2 += int(b[v])
    if m1 == m2:
        return 'билет счастливый'
    else:
        return 'билет не счастливый'
print(f(b))
