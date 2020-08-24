items1 = ['book']
items2 = []

#配列の中身の存在チェックする
if items1:
    print(items1[0])
else:
    print('None')

if items2:
    print(items2[0])
else:
    print('None2')

items3 = ['book', 'note']
#要素の存在チェック
exits_flag = 'book' in items3
print(exits_flag)

count = {'book' : 1, 'note' : 2}
exits_flag2 = 'book' in count
print(exits_flag2)
exits_flag3 = 1 in count
print(exits_flag3)