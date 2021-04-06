import time
import os
from PIL import Image
os.system("cls")
os.system("title 準備開始囉")
os.system("pause")
for a in range(1, 1295):
    time.sleep(0.08)
    IMG = "C:/Users/User/Desktop/Bad Apple/demo/0 (%s).jpg" % (a)
    WIDTH = 80
    HEIGHT = 35
    OUTPUT = "C:/Users/User/Desktop/Bad Apple/txt demo/%s.txt" % (a)
    s = "title 第%s張" % (a)
    ascii_char = list(
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

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
        print(txt)
        os.system(s)
        if OUTPUT:
            with open(OUTPUT, 'w') as f:
                f.write(txt)
        else:
            with open("output.txt", 'w') as f:
                f.write(txt)
