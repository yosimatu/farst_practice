# YIC情報ビジネス専門学校
# 情報システム科1年 吉松耕佑(B0021037@ib.yic.ac.jp)

from tkinter import *
from tkinter import ttk

def inputOperation():
    #print(f't2.get()'を登録しました。, %s.' % t.get())
    print(f'{t.get()} {t2.get()} を登録しました。')

root = Tk()
root.title('初めてのGUIアプリ')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='苗字')
label2 = ttk.Label(frame1, text='名前')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)
t2 = StringVar()
entry2 = ttk.Entry(frame1, textvariable=t2)
#
# TextField
# TextArea
#
'''
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get()))
'''
button1 = ttk.Button(
    frame1,
    text = 'OK',
    command=inputOperation)

# レイアウト
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
label2.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)


# ウィンドウの表示開始
root.mainloop()