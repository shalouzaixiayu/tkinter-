# -*- coding :  utf-8 -*-
# @Time      :  2020/4/5  0:19
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
from tkinter import *

class_item = ['数学', '语文', '英语', '地理', '物理']


# 初始化列表
def f2_ini():  # 初始化集合
    listbox.delete(0, END)
    for i in class_item:
        listbox.insert(END, i)


#  listbox.curselection() 返回光标指的位置元组 从0 开始
def f2_ins():  # 添加 插入
    if entry.get() != '':
        print(listbox.curselection())  # 确定位置
        if listbox.curselection() == ():  # 如果没选位置 添加
            listbox.insert(listbox.size(), entry.get())
            class_item.append(str(entry.get()))
        else:  # 如果选了位置 就是插入
            listbox.insert(listbox.curselection(), entry.get())
            class_item.append(str(entry.get()))
        print('现在课程', class_item)
    else:
        lable1.config(text='你还未输入课程名称')


def f2_rev():  # 修改
    if entry.get() != '' and listbox.curselection() != ():
        start = listbox.curselection()[0]
        listbox.delete(start)
        listbox.insert(start, entry.get())
        class_item[start] = str(entry.get())
        print('现在课表:', class_item)
    else:
        lable1.config(text='你还未输入更改后的课程名称')


def f2_del():  # 删除
    lable1.config(text='点击左侧的课程，再点击删除即可')
    if listbox.curselection() != ():
        start = listbox.curselection()[0]
        listbox.delete(listbox.curselection())
        class_item.pop(start)
        print('现在课程', class_item)


def f2_emp():  # 清空
    lable1.config(text='点击清空，左侧课程则全部删除')
    listbox.delete(0, END)
    class_item.clear()
    print('现在课程', class_item)


root = Tk()
root.geometry('400x300')
root.title('列表框')
frame1 = Frame(root, relief=RAISED)
frame1.place(relx=0.0)
frame2 = Frame(root, relief=GROOVE)
frame2.place(relx=0.5)
listbox = Listbox(frame1)
listbox.pack()
entry = Entry(frame2)
entry.pack()

lable1 = Label(frame2, text='输入课程进行以下操作', fg='black', font=('宋体', 10))
lable1.pack(fill=X)
btn1 = Button(frame2, text='初始化', command=f2_ini)
btn1.pack(fill=X)
btn2 = Button(frame2, text='添加', command=f2_ins)
btn2.pack(fill=X)
btn3 = Button(frame2, text='插入', command=f2_ins)
btn3.pack(fill=X)
btn4 = Button(frame2, text='修改', command=f2_rev)
btn4.pack(fill=X)
btn5 = Button(frame2, text='删除', command=f2_del)
btn5.pack(fill=X)
btn6 = Button(frame2, text='清空', command=f2_emp)
btn6.pack(fill=X)
root.mainloop()
