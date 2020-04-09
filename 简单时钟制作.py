# -*- coding :  utf-8 -*-
# @Time      :  2020/4/4  23:29
# @author    :  沙漏在下雨
# @Software  :  PyCharm

from tkinter import *
import time
import random


def get_time():
    now_time = time.strftime('%H:%M:%S', time.localtime())
    # 本地时间localtime() 
    lable1.configure(text=now_time)
    root1.after(1000, get_time)


def get_text():
    data = []
    with open('D://py词云//网易云留言板.txt', 'r') as fr:
        for i in fr:
            data.append(str(i.strip('\n').split('\t')))

    rd_data = random.choice(data).strip("[]").strip("''")
    # mess1.configure(text=rd_data)
    txt.insert(END, rd_data + '\n\n')
    root1.after(5000, get_text)


root1 = Tk()
root1.title('简易时钟留言版')
root1.geometry('400x400')
lable1 = Label(root1, text='', fg='red', font=('宋体', 50), relief=GROOVE)
lable1.pack()
get_time()

txt = Text(root1, fg='red', font=('宋体', 10), relief=GROOVE)
txt.pack()
get_text()
root1.mainloop()
