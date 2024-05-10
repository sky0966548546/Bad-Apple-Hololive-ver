from PIL import Image
from tqdm import TqdmExperimentalWarning
from tqdm.rich import trange
import os
import warnings


def get_char(r, g, b, alpha=256):
  if alpha == 0:
    return ' '

  lenght = len(ascii_char)
  gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
  unit = (256.0 + 1) / lenght

  return ascii_char[int(gray / unit)]

warnings.filterwarnings('ignore', category=TqdmExperimentalWarning)

images_path = 'assets/images'
images = os.listdir(images_path)
sorted_images = sorted(images, key=lambda x: int(x.split('.')[0]))

for i in trange(len(sorted_images)):
  WIDTH = 72
  HEIGHT = 42
  OUTPUT = f'assets/text/{i + 1}.txt'

  ascii_char = list('⠀⠄⠆⠖⠶⡶⣩⣪⣫⣾⣿')

  im = Image.open(os.path.join(images_path, sorted_images[i]))
  im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
  txt = ''

  for h in range(HEIGHT):
    for w in range(WIDTH):
      txt += get_char(*im.getpixel((w, h)))

    txt += '\n'

  with open(OUTPUT, 'w') as f:
    print(txt, file=f)