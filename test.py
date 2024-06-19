import re
import random
lst = []
with open('words_alpha.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        lst.append(word)
        
var = ''
for i in range(1,1000000):
    var += f'{lst[random.randint(1,370100)]} '
    print(i)
with open('output.txt', 'w') as f:
    f.write(var)