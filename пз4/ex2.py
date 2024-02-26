b = int(input("Введите число: "))
def f(a):
    if a == 0:
        return "на ноль делить нельзя"
    else:
        return 100 / a
print(f(b))