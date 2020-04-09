# -*- coding :  utf-8 -*-
# @Time      :  2020/4/6  21:39
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219

from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('滑动条测试')


def show(event):
    s = '滑块的取值为:' + str(sca.get())
    print(s)
    labe1.config(text=s)


var = DoubleVar()  # 滑块类型框架
sca = Scale(root, orient=HORIZONTAL, length=200, from_=1.0,
            to=5.0, label='请拖动滑块', resolution=0.05, tickinterval=1,
            variable=var)
sca.bind('<ButtonRelease-1>', show)  # 松开鼠标左键事件
sca.pack()

labe1 = Label(root, text='')
labe1.pack()

root.mainloop()
