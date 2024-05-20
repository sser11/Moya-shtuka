def z1():
    import json
    with open('products.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        n = 0
        for i in a['products']:
            print(f'Название: {i['name']}')
            print('')
            print(f'Цена: {i['price']}')
            print('')
            print(f'Вес: {i['weight']}')
            print('')
            if str(i['available']) == "True":
                print('В наличии')
            else:
                print('Нет в наличии')
            print('')
            print('--------------------')
            print('')

def z2():
    import json
    with open('products.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        new = {
            'name': input('Введите название нового продукта: '),
            'price' : input('Введите цену нового продукта: '),
            'weight' : input('Введите вес нового продукта: '),
            'available' : input('Продукт в наличие? (True/False): ')
        }
        a['products'].append(new)
        with open('products.json', 'w', encoding='utf-8') as d:
            json.dump(a, d, indent = 4)
    with open('products.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        n = 0
        for i in a['products']:
            print(f'Название: {i['name']}')
            print('')
            print(f'Цена: {i['price']}')
            print('')
            print(f'Вес: {i['weight']}')
            print('')
            if str(i['available']) == "True":
                print('В наличии')
            else:
                print('Нет в наличии')
            print('')
            print('--------------------')
            print('')

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    rus_eng = {}
    for line in lines:
        if '-' in line:
            eng_word, ru_tr = line.strip().split('-')
            for ru_word in ru_tr.split(','):
                if ru_word.strip() not in rus_eng:
                    rus_eng[ru_word.strip()] = [eng_word]
                else:
                    if eng_word not in rus_eng[ru_word.strip()]:
                        rus_eng[ru_word.strip()].append(eng_word)
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for key in sorted(rus_eng.keys()):
            trans = ','.join(sorted(rus_eng[key]))
            file.write(f'{key}-{trans}\n')
z3()