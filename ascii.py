import os
from PIL import Image
for a in range(1, 2):
    IMG = "C:/Users/User/Desktop/Bad Apple/data/%s.jpg" % (a)
    WIDTH = 300
    HEIGHT = 82
    OUTPUT = "C:/Users/User/Desktop/Bad Apple/txt/%s.txt"%(a)
    ascii_char = list("⠀⠄⠆⠖⠶⡶⣩⣪⣫⣾⣿")
    def get_char(r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        lenght = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1)/lenght
        return ascii_char[int(gray/unit)]
    if __name__ == '__main__':
        im = Image.open(IMG)
        im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
        txt = ""

        for h in range(HEIGHT):
            for w in range(WIDTH):
                txt += get_char(*im.getpixel((w, h)))
            txt += '\n'

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            print("輸出第",a,"張")
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            print("輸出第",a,"張")
            f.write(txt)
