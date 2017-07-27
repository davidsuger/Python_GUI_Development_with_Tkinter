#!/usr/bin/python3
# text.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

root = Tk()

text = Text(root, width=40, height=10)
text.pack()
text.config(wrap='word')
text.insert(1.0, '''明細（借方）を複数に分けたい**SBR**220****SBR1234**PROJYEC**2U**A99999**コネクトツウシン
**KESHIKOMI**20171231**税込（８％）**西口単票入力テスト
******20170412テストデータ大２
含まない**設備工事**自社使用・資本的支出*******4****3**使用期間**１年未満**`
G1標準支払**SBU**S560**176215****SBV1111****SHD**A30987**iK07）全額期日105日サイト**17/１宅急便代**ASDFGH**20170410**1008942**N 納品書検収**5
123**2345**456**20**2**4**9876**100**300**20170410**60
1**14621**10000**SHD**E23093**1**Å(5%)****3********P93**E230****************テスト１******2**283**2000**SBU**E23091**2**Å(5%)************P91**E230****************テスト２******3**220**3000**SCS**L153**3**Å(5%)**2****************************テスト３''')
print(text.get('1.0', 'end'))
print(text.get('1.0', '1.end'))

text.insert('1.0 + 2 lines', 'Inserted message ')
text.insert('1.0 + 2 lines lineend', 'and\nmore and\nmore...')
text.delete('1.0')
text.delete('1.0', '1.0 lineend + 1 chars')

text.replace('1.0', '1.0 lineend', 'This is the first line.')
text.config(state='disabled')
text.delete('1.0', 'end')
text.config(state='normal')

text.tag_add('my_tag', '1.0', '1.0 wordend')
print(text.tag_ranges('my_tag'))

text.tag_configure('my_tag', background='yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())
print(text.tag_names('1.0'))
text.replace('my_tag.first', 'my_tag.last', 'That')
text.tag_delete('my_tag')

print(text.mark_names())

text.insert('insert', '++')
text.mark_set('my_mark', '1.0')

text.mark_gravity('my_mark', 'right')
text.insert('my_mark', '+-')
text.insert('my_mark', 'ab')
text.mark_unset('my_mark')

image = PhotoImage(file='python_logo.gif')
text.image_create('1.0', image=image)

button = Button(text, text='Click Me')
text.window_create('1.0', window=button)

root.mainloop()
