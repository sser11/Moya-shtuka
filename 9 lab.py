def z1():
    from pathlib import Path
    from PIL import Image
    input_dir = Path(r'Z:\1-мд-21\Чыпсымаа Олег\img\a')
    output_dir = Path(r'Z:\1-мд-21\Чыпсымаа Олег\img\b')
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in input_dir.iterdir():
        if file.suffix in ['.jpg', '.png', '.bmp']:
            input_path = file
            output_path = output_dir / file.name
            image = Image.open(input_path)
            image = image.convert('1')
            image.save(output_path)
    print("Всё обработано!")

def z2():
    import os
    from pathlib import Path
    from PIL import Image
    input_dir = Path(r'Z:\1-мд-21\Чыпсымаа Олег\img\a')
    input_files = os.listdir(input_dir)
    output_dir = Path(r'Z:\1-мд-21\Чыпсымаа Олег\img\b')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        for file in input_files:
            extension = os.path.splitext(file)[1]
        if extension.lower() in ['.jpg', '.png']:
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            image = Image.open(input_path)
            image = image.convert('50')
            image.save(output_path)
    print("Всё обработано!")

def z3():
    import csv
    with open('xleb.csv', 'r', encoding='utf-8') as a:
        reader = csv.reader(a)
        print('Нужно купить:')
        print('')
        max1 = 0
        max2 = 0
        max3 = 0
        for j in reader:
            if len(j[0]) > max1:
                max1 = len(j[0])
            if len(j[1]) > max2:
                max2 = len(j[1])
            if len(j[2]) > max3:
                max3 = len(j[2])
    with open('xleb.csv', 'r', encoding='utf-8') as a:
        reader = csv.reader(a)
        i = 0
        n1 = 0
        n2 = 0
        n3 = 0
        for row in reader:
            n1 = max1 - len(row[0])
            n2 = max2 - len(row[1])
            n3 = max3 - len(row[2])
            for i in range(n1):
                row[0] = row[0] + ' '
            for i in range(n2):
                row[1] = row[1] + ' '
            for i in range(n3):
                row[2] = row[2] + ' '
            print(f'| {row[0]} | {row[1]} шт. | {row[2]} руб. |')
            i += int(row[1]) * int(row[2])
        print(f'Итоговая сумма: 800')