def f1():
    from PIL import Image
    a = "cat.jpg"
    with Image.open(a) as img:
        img.load()
    img.show()
    w, h = img.size
    format = img.format
    mode = img.mode
    print('Ширина: ',w)
    print('Высота: ',h)
    print('Формат: ', format)
    print('Цветовой мод: ',mode)

def f2():
    from PIL import Image
    b = 'cat.jpg'
    with Image.open(b) as img:
        img.load()
    img2 = img.resize((img.width //3, img.height //3))
    img2.save('cat2.jpg')

def f3():
    from PIL import Image, ImageFilter
    for i in range(1, 6):
        i = str(i)
        img = Image.open(i + '.jpg')
        img = img.filter(ImageFilter.EMBOSS)
        img.save("D:\питон\pics\img" + i + ".jpg")

def f4():
    from PIL import Image
    img = Image.open('1.jpg')
    wm = Image.open('cavabanga.png')
    img.paste(wm, (300,230), wm)
    img.save('ababba.jpg')