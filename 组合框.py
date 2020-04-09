# -*- coding :  utf-8 -*-
# @Time      :  2020/4/6  19:33
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219

from tkinter import *
from tkinter.ttk import *  # 组合框对象 子模块

root = Tk()
root.geometry('300x400')
root.title('简单四则运算')


def calc(event):
    a = float(inp1.get())
    b = float(inp2.get())
    data_items = {0: a + b, 1: '{:.5f}'.format(a - b),
                  2: '{:.5f}'.format(a * b), 3: '{:.5f}'.format(a / b)}
    ans = '答案显示: ' + str(data_items[comb.current()])  # 获得选择的索引序号
    print(ans)
    lab4.config(text=ans)


lab1 = Label(root, text='数字一:', font=('宋体', 10))
lab2 = Label(root, text='数字二:', font=('宋体', 10))
inp1 = Entry(root)
inp2 = Entry(root)

lab1.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.1)
lab2.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
inp1.place(relx=0.4, rely=0.13, relwidth=0.2, relheight=0.05)
inp2.place(relx=0.4, rely=0.22, relwidth=0.2, relheight=0.05)

lab3 = Label(root, text='运算操作:', font=('宋体', 10))
lab3.place(relx=0.2, rely=0.33, relwidth=0.2, relheight=0.05)

var = StringVar()  # 创建一个 组合框 对象框架

comb = Combobox(root, textvariable=var, values=['加法', '减法', '乘法', '除法'])
# 加入var控件属性
comb.place(relx=0.4, rely=0.33, relwidth=0.2, relheight=0.05)
comb.bind('<<ComboboxSelected>>', calc)  # 鼠标时间 调用组合框函数

lab4 = Label(root, text='答案显示: ******', font=('宋体', 10))
lab4.place(relx=0.2, rely=0.45, relheight=0.05)

root.mainloop()
