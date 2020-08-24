items = [1,2,3]

#ループ
for i in items:
    print(f'変数iの値は{i}')

for i in range(4):
    print(f'{i}回目の処理')

chars = 'hello world'
for count, char in enumerate(chars):
    print(f'{count}番目の文字は、{char}')

nums = [2,4,6]
for i in nums:
    if i % 2 == 0:
        print('偶数あり')
        break
else:
    print('偶数無し')

for i in nums:
    if i % 2 == 1:
        print('奇数あり')
        break
else:
    print('奇数無し')

#i が最後に入っている値を確認する
#for文の使用時には気を付けます
print(i)