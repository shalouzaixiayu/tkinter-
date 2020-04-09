from tkinter import *
import time


def insert_time():
    now_time = str(time.strftime('%Y:%m:%d---%H:%M:%S', time.localtime()))
    text1.insert(END, now_time + '\n')
    root1.after(2000, insert_time)


root1 = Tk()
root1.title('时间追加器')
root1.geometry('400x400')
label1 = Label(root1, text='下面演示text的追加时间信息', fg='red',
               font=('宋体', 10))
label1.pack()

text1 = Text(root1)
text1.pack()
insert_time()

root1.mainloop()
