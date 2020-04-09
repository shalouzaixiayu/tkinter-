from tkinter import *

root = Tk()
root.geometry('400x200')
root.title('简易乘法器')


def fun1():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '{:.2f} * {:.2f} = {:.2f}\n'.format(a, b, a * b)
    text1.insert(END, s)  # 追加显示文本信息
    inp1.delete(0, END)  # 清空
    inp2.delete(0, END)


def fun2(a, b):
    s = '{:.2f} * {:.2f} = {:.2f} \n'.format(float(a), float(b), float(a) * float(b))
    text1.insert(END, s)
    inp1.delete(0, END)
    inp2.delete(0, END)


lab1 = Label(root, text='请在二个框内各输入一个数，二种方法供给选择')
lab1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

inp1 = Entry(root)  # 定义第一个输入框
inp1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

inp2 = Entry(root)  # 定义第二个输入框
inp2.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.1)

# 定义第一个按钮
btn1 = Button(root, text='F1:不传值', command=fun1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)

# 定义第二个按钮
btn2 = Button(root, text='F2:传值', command=lambda: fun2(inp1.get(), inp2.get()))
btn2.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)

# 在窗口垂直自上而下位置60%处， 建立一个相当整体窗体的40%的文本框

text1 = Text(root)
text1.place(rely=0.6, relheight=0.4)

root.mainloop()
