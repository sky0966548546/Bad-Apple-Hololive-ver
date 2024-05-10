import os
import time


os.system('pause')
time.sleep(0.1)

path = 'assets/text'
texts = os.listdir(path)
sorted_text = sorted(texts, key=lambda x: int(x.split('.')[0]))

fps = 1 / 30
start_time = time.time()

for text in sorted_text:
  with open(os.path.join(path, text), 'r', encoding='UTF-8') as file:
    os.system('cls')
    print(f'{file.read()}')

  elapsed_time = time.time() - start_time

  if elapsed_time < fps:
    time.sleep(fps - elapsed_time)

  start_time = time.time()