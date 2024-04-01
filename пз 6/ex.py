def a():
    a = dict(Russia = 'Moskow', China = 'Beijing', Argentina = 'Buenos Aires')
    print(a)
    print(a['Russia'])
    a = dict(sorted(a.items()))
    print(a)
def b():
    str1 = 'авеинорст'
    a = {}
    for i in str1:
        a[i] = 1
    str2 = 'дклмпу'
    for i in str2:
        a[i] = 2
    str3 = 'бгёья'
    for i in str3:
        a[i] = 3
    str4 = 'йы'
    for i in str4:
        a[i] = 4
    str5 = 'жзхцч'
    for i in str5:
        a[i] = 5
    str6 = 'шэю'
    for i in str6:
        a[i] = 8
    str7 = 'фщъ'
    for i in str7:
        a[i] = 10
    b = input('Введите своё слово: ')
    n = 0
    for i in b:
        n += a[i]
    print(n)
def c():
    n = []
    m = []
    a = ''
    while a != 'end':
        a = input(f'Имя студента:'
                  f'')
        if a == 'end':
            break
        b = input(f'Сколько языков вы знаете?'
                  f'')
        for i in range(int(b)):
            j = input('Напишите один из языков, который Вы знаете:'
                      '')
            if m.count(j) == 0:
                m.append(j)
            if j == 'китайский':
                n.append(a)
    print(n)
    print(sorted(m))