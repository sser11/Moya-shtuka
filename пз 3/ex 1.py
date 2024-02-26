a = ''
n= int(input("Сколько будет слов? "))
for i in range(n):
    f = input('Введите слово: ')
    if f == '':
        print('Введите слово верно!')
    else:
        a += f + ' '
print(a)