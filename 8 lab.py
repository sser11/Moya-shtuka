from PIL import Image, ImageDraw, ImageFont

def z1():
    def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    im = Image.open(r'Z:\1-мд-21\Чыпсымаа Олег\ng.jpg')
    im_new = crop_center(im, 1000, 1800)
    im_new.save(r'Z:\1-мд-21\Чыпсымаа Олег\ng1.jpg', quality=200)
    im_new.show()


def z2():
    party = {
        "НГ" : r"Z:\1-мд-21\Чыпсымаа Олег\ng.jpg",
        "8 марта":r"Z:\1-мд-21\Чыпсымаа Олег\mart.jpg",
        "23 февраля":r"Z:\1-мд-21\Чыпсымаа Олег\feb.jpg"
    }
    x = input("введите праздник: ")
    for key in party:
        if key == x:
            print("Открытка загружается")
            y = Image.open(party[key])
            y.show()


def z3():
    party = Image.open(r'Z:\1-мд-21\Чыпсымаа Олег\mart.jpg')
    imdraw = ImageDraw.Draw(party)
    x = input("введите имя: ")
    text = str(x) + ', поздравляю! '
    font_path = r"Z:\1-мд-21\Чыпсымаа Олег\Kablammo-Regular-VariableFont_MORF.ttf"
    font = ImageFont.truetype(font_path, size=50)
    y = imdraw.textlength(text, font=font)
    z = party.size
    w = (z[0] // 2) - (y // 2)
    imdraw.text((w, 10), text, font=font, fill=("#ff1111"))
    party.save(r'Z:\1-мд-21\Чыпсымаа Олег\mart1.png')
    party.show()
