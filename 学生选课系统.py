# -*- coding :  utf-8 -*-
# @Time      :  2019/12/22  10:41
# @author    :  沙漏在下雨
# @Software  :  PyCharm
from tkinter import *
import time
import os


def choosefile(i16, i17, i181, i182, i183, i184, i185, i186, text3, ip16, ip17, ip181, ip182, ip183, ip184, ip185,
               ip186):
    # 将学生选好的课程 对应他的学号姓名， 一样的写入到文件里面  成功实现
    print(i16)  # 检验传值是否成功
    class_list = []  # 总课程列表
    class_list0 = []  # 暂存
    with open("D://课程//课程信息.txt", "r") as kc:
        for i in kc:
            s = i.strip("\n").split("\t")  # 取文件里面每一行去掉空格 去掉换行 后的列表
            # print(s[1])  #课程名称:大学语文
            class_list0.append(str(s[1]))
        for j in class_list0:
            # print(j[5:9])
            class_list.append(str(j[5:9]))
        print(class_list)  # 课程一共长度为5 这个也是课程总列表

    number_list = []  # 总学号列表
    number_list0 = []  # 暂存区 = =
    with open("D://课程//课程信息.txt", "r") as xh:
        for i in xh:
            s = i.strip("\n").split("\t")  # 取文件里面每一行去掉空格 去掉换行 后的列表
            print(s[1])  # 学生学号:0001
            number_list0.append(str(s[1]))
        for jj in number_list0:
            print(jj[6:10])
            number_list.append(str(jj[6:10]))
    # print(class_list)  # 学号一共长度 这个也是学号总列表
    nl = set(number_list)  # 将学号形成集合   然后进行判断
    print(nl)

    if not os.path.exists("D://课程//"):  # 判断这个目录是否存在
        os.mkdir("D://课程//")  # 建立这个目录
    else:
        s = "学生姓名:{}\t 学生学号:{}\t  课程一:{}\t课程二:{}\t课程三:{}\t课程四:{}\t课程五:{}\t课程六:{}\n".format(i16, i17, i181, i182, i183,
                                                                                           i184, i185, i186)
        ss = "学生:{}的选课信息已经保存成功!(D://课程//学生选课信息.txt)\n".format(i16)
        sss = "学生:{}所选的课程包含未录入课程或未选满课程！\n".format(i16)
        ssss = "学生:{}对应的学号已经存在!\n".format(i16)
        # 判断总分之和是否大于60分数  这个功能太监了
        if i16:  # 排除空值
            if i17:  # 判空
                if str(i17) in nl:  # 判断输入的学号是否已存在
                    text3.insert(END, ssss)

                if str(i181) and str(i182) and str(i183) and str(i184) and str(i185) and str(
                        i186) in class_list:  # 判断课程是否存在
                    with open("D://课程//学生选课信息.txt", "a") as of:
                        of.write(s)
                        of.close()
                        text3.insert(END, ss)  # 显示追加效果
                        ip16.delete(0, END)  # 清空输入
                        ip17.delete(0, END)  # 清空输入
                        ip181.delete(0, END)  # 清空输入
                        ip182.delete(0, END)  # 清空输入
                        ip183.delete(0, END)  # 清空输入
                        ip184.delete(0, END)  # 清空输入
                        ip185.delete(0, END)  # 清空输入
                        ip186.delete(0, END)  # 清空输入
                else:  # 追加其他信息
                    text3.insert(END, sss)  # 显示追加效果


def lurufile(aa, b, c, d, e, f, text1, a8, a9, a10, a11, a12, a13):  # 写入到文件 成功!
    print(b)  # 检验传值是否成功
    if not os.path.exists("D://课程//"):  # 判断目录是否存在
        os.mkdir("D://课程//")  # 建立这个目录
    else:
        s = "课程编号:{}\t课程名称:{}\t课程性质:{}\t任课老师:{}\t课程学分:{}\t开课时间:{}\n".format(aa, b, c, d, e, f)
        ss = "课程:{}已经录入成功!(D://课程//课程信息.txt)\n".format(b)
        if aa:  # 排除空值
            with open("D://课程//课程信息.txt", "a+") as fo:
                fo.write(s)
                text1.insert(END, ss)  # 追加显示运算结果
                a8.delete(0, END)  # 清空输入
                a9.delete(0, END)  # 清空输入
                a10.delete(0, END)  # 清空输入
                a11.delete(0, END)  # 清空输入
                a12.delete(0, END)  # 清空输入
                a13.delete(0, END)  # 清空输入


def namefind(i19, inp19, text4):  # 按照学生姓名查询文件 然后返回到find定义的文本框中
    print(i19)  # 检验传值是否成功
    with open("D://课程//学生选课信息.txt", "r") as ff:  # 遍历这个txt把
        for i in ff:  # 遍历文件的每一行 进行判断
            if i19:  # 判空
                if str(i19) in i:
                    text4.insert(END, i + '\n')
                    inp19.delete(0, END)


def classfind(i20, inp20, text4):  # 按照学生学号来查询，
    print(i20)  # 检验传值是否成功
    with open("D://课程//学生选课信息.txt", "r") as ff:  # 遍历这个txt把
        for i in ff:
            if len(str(i20)) == 4:  # 判断这个学号真的是学号
                if str(i20) in i:  # 判断学号是否在选课信息
                    text4.insert(END, i + "\n")
                    inp20.delete(0, END)


def luru():  # 录入函数
    print("录入")
    winNew1 = Toplevel()
    winNew1.title("录入课程模式")
    winNew1.geometry(align_str)  # 设置窗口大小 和原窗口一样
    winNew1.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    label_6 = Label(winNew1, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE).pack()
    label_7 = Label(winNew1, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
    # 设置警告备注
    label_00 = Label(winNew1, text="PS:在校学生课程学分总和不得少于60分！输入课程学分请谨慎！", font=("宋体", 10))
    label_00.place(relx=0, rely=0.2)
    label_8 = Label(winNew1, text="课程编号:", font=("宋体", 10)).place(relx=0, rely=0.3)
    label_9 = Label(winNew1, text="课程名称:", font=("宋体", 10)).place(relx=0.5, rely=0.3)
    label_10 = Label(winNew1, text="课程性质:", font=("宋体", 10)).place(relx=0, rely=0.4)  # 专业 还是 公开
    label_11 = Label(winNew1, text="任课老师:", font=("宋体", 10)).place(relx=0.5, rely=0.4)
    label_12 = Label(winNew1, text="课程学分:", font=("宋体", 10)).place(relx=0, rely=0.5)
    label_13 = Label(winNew1, text="开课时间:", font=("宋体", 10)).place(relx=0.5, rely=0.5)
    inp8 = Entry(winNew1)  # 定义8输入框
    inp8.place(relx=0.15, rely=0.3)
    inp9 = Entry(winNew1)  # 定义9输入框
    inp9.place(relx=0.65, rely=0.3)
    inp10 = Entry(winNew1)  # 定义10输入框
    inp10.place(relx=0.15, rely=0.4)
    inp11 = Entry(winNew1)  # 定义11输入框
    inp11.place(relx=0.65, rely=0.4)
    inp12 = Entry(winNew1)  # 定义12输入框
    inp12.place(relx=0.15, rely=0.5)
    inp13 = Entry(winNew1)  # 定义13入框
    inp13.place(relx=0.65, rely=0.5)
    text1 = Text(winNew1, bg="#d3fbfb")  # 打印文本
    text1.place(rely=0.7)
    btn2 = Button(winNew1, text='确定',
                  command=lambda: lurufile(inp8.get(), inp9.get(), inp10.get(), inp11.get(), inp12.get(), inp13.get(),
                                           text1,
                                           inp8, inp9, inp10, inp11, inp12, inp13))  # 确定按钮
    btn2.place(relx=0.35, rely=0.6)
    btClose2 = Button(winNew1, text='关闭', command=winNew1.destroy)  # 取消按钮
    btClose2.place(relx=0.55, rely=0.6)


def choose():  # 选择函数
    print("选择")
    winNew3 = Toplevel()
    winNew3.geometry(align_str)  # 设置窗口大小 和原窗口一样
    winNew3.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew3.title('选择课程模式')
    label_a = Label(winNew3, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE).pack()
    label_b = Label(winNew3, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
    # 定义上面的窗口界面
    # 我们假定一个人最多就只能选择5~6门课程
    label_15 = Label(winNew3, text="PS:在校学生请选择5至6门课程,且学分总和不得少于60分！", font=("宋体", 10)).place(relx=0, rely=0.2)
    label_16 = Label(winNew3, text="输入学生姓名:", font=("宋体", 10)).place(relx=0.2, rely=0.3)
    label_17 = Label(winNew3, text="输入学生学号:", font=("宋体", 10)).place(relx=0.2, rely=0.4)
    ps = Label(winNew3, text="(规定学号长度为4位)", font=("黑体", 8)).place(relx=0.16, rely=0.46)
    label_18 = Label(winNew3, text="输入课程名称(1-6):", font=("宋体", 10)).place(relx=0.13, rely=0.5)
    # 下面定义所有的输入框
    inp16 = Entry(winNew3)  # 定义16输入框 姓名
    inp16.place(relx=0.38, rely=0.3)
    inp17 = Entry(winNew3)  # 定义17输入框 学号
    inp17.place(relx=0.38, rely=0.4)
    inp181 = Entry(winNew3)  # 定义181输入框 课程1
    inp181.place(relx=0.38, rely=0.5)
    inp182 = Entry(winNew3)  # 定义182输入框 课程2
    inp182.place(relx=0.68, rely=0.5)
    inp183 = Entry(winNew3)  # 定义183输入框 课程3
    inp183.place(relx=0.38, rely=0.55)
    inp184 = Entry(winNew3)  # 定义184输入框 课程3
    inp184.place(relx=0.68, rely=0.55)
    inp185 = Entry(winNew3)  # 定义185输入框 课程5
    inp185.place(relx=0.38, rely=0.6)
    inp186 = Entry(winNew3)  # 定义186输入框 课程6
    inp186.place(relx=0.68, rely=0.6)
    text3 = Text(winNew3, bg="#d3fbfb")
    text3.place(rely=0.73)  # 定义第三个文本框
    # 定义确定和推出按钮
    btn3 = Button(winNew3, text='确定', command=lambda: choosefile(inp16.get(), inp17.get(), inp181.get(),
                                                                 inp182.get(), inp183.get(), inp184.get(), inp185.get(),
                                                                 inp186.get(), text3, inp16, inp17, inp181,
                                                                 inp182, inp183, inp184, inp185, inp186))
    # 确定按钮 然后把所有值 送到choosefile中  同样写入文件
    btn3.place(relx=0.38, rely=0.65)
    btClose3 = Button(winNew3, text='关闭', command=winNew3.destroy)  # 关闭按钮
    btClose3.place(relx=0.68, rely=0.65)


def look():  # 浏览函数
    print("浏览")
    winNew2 = Toplevel()
    winNew2.geometry(align_str)  # 设置窗口大小 和原窗口一致
    winNew2.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew2.title('浏览课程模式')
    label_a = Label(winNew2, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE).pack()
    label_b = Label(winNew2, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
    # 定义上面的窗口界面
    text2 = Text(winNew2, bg="#d3fbfb")
    text2.place(rely=0.3)
    with open("D://课程//课程信息.txt", "r") as kc:  # 打开文件
        for i in kc:  # 遍历这个txt
            text2.insert(END, i + "\n")
    btClose3 = Button(winNew2, text='关闭', command=winNew2.destroy)  # 取消按钮
    btClose3.place(relx=0.7, rely=0.2)


def find():  # 查询函数
    print("查询")
    winNew4 = Toplevel()
    winNew4.geometry(align_str)  # 设置窗口大小 和原窗口一致
    winNew4.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew4.title('查询信息模式')
    label_a = Label(winNew4, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE).pack()
    label_b = Label(winNew4, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
    # 定义上面的窗口界面
    # 定义下面二种查询方式   通过姓名查询  或者通过课程查询  其他方式没想到
    label_19 = Label(winNew4, text="按学生姓名查询:", font=("宋体", 10))
    label_19.place(relx=0.25, rely=0.3)
    label_20 = Label(winNew4, text="按学生学号查询:", font=("宋体", 10))
    label_20.place(relx=0.25, rely=0.4)
    # 定义二个输入输入框
    inp19 = Entry(winNew4)
    inp19.place(relx=0.45, rely=0.3)  # 学生姓名传值
    inp20 = Entry(winNew4)
    inp20.place(relx=0.45, rely=0.4)  # 学生学号传值
    # 定义二个确定按钮
    btn4 = Button(winNew4, text="确定", command=lambda: namefind(inp19.get(), inp19, text4))  # 学生姓名确定
    btn4.place(relx=0.75, rely=0.28)
    btn5 = Button(winNew4, text="确定", command=lambda: classfind(inp20.get(), inp20, text4))  # 学生学号确定
    btn5.place(relx=0.75, rely=0.39)
    # 写一个备注ps
    ps = Label(winNew4, text="PS:若文本框未显出信息,则该学生选课信息未成功保存,请重试！", font=("宋体", 10))
    ps.place(relx=0, rely=0.52)
    # 定义一个关闭按钮
    btClose4 = Button(winNew4, text='关闭', command=winNew4.destroy)  # 取消按钮
    btClose4.place(relx=0.75, rely=0.5)
    # 定义下面的文本框
    text4 = Text(winNew4, bg="#d3fbfb")
    text4.place(rely=0.6)


def menu(var):  # 菜单返回函数
    print(var)  # 检测函数返回值
    if var == 0:
        luru()  # 录入函数
    elif var == 1:
        look()  # 课程浏览
    elif var == 2:
        choose()  # 课程选择
    else:
        find()  # 课程查询


def new_windows(windows):  # 登入界面成功后的窗口
    winNew = Toplevel()
    winNew.geometry(align_str)  # 设置窗口大小保持和主窗口相同
    winNew.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew.title('系统菜单模式')
    label_a = Label(winNew, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE).pack()
    label_b = Label(winNew, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
    # 二个一样的标签  下面设置功能模块
    var = IntVar()  # 设置选择属性 下面为单选框各模块
    rd1 = Radiobutton(winNew, text="课程录入", variable=var, value=0, command=lambda: menu(var.get()))
    rd1.place(relx=0.4, rely=0.3)  # 标签课程录入

    rd2 = Radiobutton(winNew, text="课程浏览", variable=var, value=1, command=lambda: menu(var.get()))
    rd2.place(relx=0.4, rely=0.4)  # 标签课程浏览

    rd3 = Radiobutton(winNew, text="课程选择", variable=var, value=2, command=lambda: menu(var.get()))
    rd3.place(relx=0.4, rely=0.5)  # 标签课程选择

    rd4 = Radiobutton(winNew, text="课程查询", variable=var, value=3, command=lambda: menu(var.get()))
    rd4.place(relx=0.4, rely=0.6)  # 标签课程查询
    btClose = Button(winNew, text='关闭程序', command=winNew.destroy)
    btClose.place(relx=0.7, rely=0.7)


def get_time():  # 屏幕刷新时间
    time_str = time.strftime("%H:%M:%S", time.localtime())  # 获得系统现在时间
    label_4.configure(text=time_str)  # 重新设置文本标签
    my_windows.after(1000, get_time)


def run(x):  # 确定账号
    a = x
    if inp1.get() == "沙漏在下雨" and inp2.get() == "123123":  # 判断用户是否正确
        s = "尊敬的客户:{}你已经登入成功进入该系统！\n".format(a)
        txt.insert(END, s)  # 追加显示运算结果
        inp1.delete(0, END)  # 清空输入
        inp2.delete(0, END)  # 清空输入
        new_windows(my_windows)  # 进去新界面
    else:
        s = "信息输入错误！请重新输入！\n"
        txt.insert(END, s)  # 追加显示运算结果
        inp1.delete(0, END)  # 清空输入
        inp2.delete(0, END)  # 清空输入


def bi_gon1():  # 彩蛋
    s = '加油加油每一天'
    bi_gon.config(text=s)


my_windows = Tk()  # 初始化TK()
my_windows.title("学生选课系统")  # 设置标题
width = 500
height = 400
# 获取屏幕尺寸以计算布局参数，让窗口位于屏幕中央
screenwidth = my_windows.winfo_screenwidth()
screenheight = my_windows.winfo_screenheight()
align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

my_windows.geometry(align_str)  # 设置窗口大小

my_windows.resizable(width=True, height=True)
# 设置窗口是否可变长、宽，True：可变，False：不可变

label_0 = Label(my_windows, text="学生选修课程系统设计", bg="#00BFFF", fg="red", font=("宋体", 30), relief=GROOVE)
label_0.pack()
label_1 = Label(my_windows, text="---------请开始选择课程之旅！---------", font=("宋体", 20)).pack()
# 二个标题之上
inp1 = Entry(my_windows)  # 定义第一个输入框
inp1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(my_windows, show="*", )  # 定义第二个输入框  且密码隐藏
inp2.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

inp_label1 = Label(my_windows, text="账号:", font=("宋体", 20))  # 定义账号
inp_label1.place(relx=0.20, rely=0.20)
inp_label2 = Label(my_windows, text="密码:", font=("宋体", 20))  # 定义密码
inp_label2.place(relx=0.20, rely=0.30)

btn1 = Button(my_windows, text='登入系统', command=lambda: run(inp1.get()))  # 登入系统的按钮
btn1.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)
label_3 = Label(my_windows, text="原创作品谢谢支持！学习交流QQ:884427640", font=("宋体", 10))
label_3.place(relx=0.26, rely=0.5)
label_4 = Label(my_windows, text=" ", fg="blue", font=("黑体", 20))
label_4.place(relx=0.37, rely=0.55)
get_time()
#  定义一个娱乐彩蛋
bi_gon = Button(my_windows, text="点我点我,有惊喜！", font=("宋体", 10), command=bi_gon1)
bi_gon.place(relx=0.65, rely=0.56)

txt = Text(my_windows, bg="#d3fbfb")  # 定义文本框
txt.place(rely=0.65, relheight=0.4)
my_windows.mainloop()
