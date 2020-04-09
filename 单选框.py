from tkinter import *


# 返回变量variable=var通常应预先声明变量的类型var=IntVar()或var=StringVar(),
# 在所调用的函数中方可用var.get()方法获取被选中实例的value值
def mysel():
    dic = {0: '甲', 1: '乙', 2: '丙', 3: "丁"}
    s = "您选了" + dic[var.get()] + "项"
    # s = "您选了" + dic.get(var.get()) + "项"   用字典里面的get()
    # lb.config(text = s)   2选1  覆盖原先的值
    lb.configure(text=s)


root = Tk()  # 初始化 Tk
root.geometry("500x300")  # 设置窗体大小
root.title('单选按钮')  # 标题
lb = Label(root, text="开始你的单选应答吧！", fg="red", font=("宋体", 20))  # 设置开头标签
lb.pack()

var = IntVar()  # 预先声明变量var
rd1 = Radiobutton(root, text="甲", variable=var, value=0, command=mysel)
rd1.pack()  # 标签甲

rd2 = Radiobutton(root, text="乙", variable=var, value=1, command=mysel)
rd2.pack()  # 标签乙

rd3 = Radiobutton(root, text="丙", variable=var, value=2, command=mysel)
rd3.pack()  # 标签丙

rd4 = Radiobutton(root, text="丁", variable=var, value=3, command=mysel)
rd4.pack()  # 标签丁
root.mainloop()
