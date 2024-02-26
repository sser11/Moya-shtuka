a = ''
n = ''
while n != 'stop':
    n = input('Введите слово: ')
    if n != 'stop' and n != '':
        a += n + ' '
print(a)