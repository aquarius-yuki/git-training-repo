import random

n = 0

while n < 3:
    print(n)
    n += 1
else:
    print('終了')

items = ['note' , 'notebook', 'sketchbook']

for item in items:
    if 'book' not in item:
        continue
    print(item)

if item := random.choice(items):
    print(item)
else:
    print('NONE')