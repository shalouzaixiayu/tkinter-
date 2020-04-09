from tkinter import *
import tkinter.messagebox  # 消息对话框
from tkinter.simpledialog import *  # 输入对话框
import tkinter.filedialog  # 文件对话框
import os
import tkinter.colorchooser  # 颜色对话框
from PIL import Image, ImageTk
import cv2

root = Tk()
root.geometry('300x300')
root.title('模拟记事本')

labe1 = Label(root, text='显示信息', fg='red', font=('宋体', 20))
labe1.place(relx=0.3, rely=0.3)


def new():
    s = '新建'
    labe1.config(text=s)


def ope():
    s = '打开'
    labe1.config(text=s)


def sav():
    s = '保存'
    labe1.config(text=s)


def cut():
    s = '剪切'
    labe1.config(text=s)


def copy():
    s = '复制'
    labe1.config(text=s)


def pas():
    s = '粘贴'
    labe1.config(text=s)


def postmenu(event):
    Main_menu.post(event.x_root, event.y_root)
    print(event.x_root, event.y_root)


def new_root():  # 新窗口
    root1 = Toplevel(root)  # 子窗口实例
    root1.geometry('300x300')
    root1.title('新窗口')
    labe2 = Label(root1, text='这是新的窗口', fg='red', font=('宋体', 20))
    labe2.place(relx=0.2, rely=0.2)
    btn_close = Button(root1, text='退出', command=root1.destroy)
    btn_close.place(relx=0.2, rely=0.35)


def mess():  # 消息对话框
    def mess1():
        ans = tkinter.messagebox.askyesno('title', 'please choose your answer!')
        # 第一个参数是标题 第二个参数是提示信息
        if ans:  # 如果选了ok
            labe1.config(text='已确定')
        else:
            labe1.config(text='已取消')

    btn1 = Button(root, text='弹出消息对话框', command=mess1)
    btn1.place(relx=0.2, rely=0.2)
    btn2 = Button(root, text='退出', command=root.destroy)
    btn2.place(relx=0.7, rely=0.2)


def key_test():  # 按键测试
    def show(event):  # 测试
        s = event.keysym
        labe2.config(text=s)

    root1 = Toplevel(root)
    root1.geometry('300x300')
    root1.title('新窗口')
    labe2 = Label(root1, text='请按键', font=('宋体', 30))
    labe2.bind('<KeyPress>', show)  # 键盘触发事件
    labe2.pack()
    labe2.focus_set()  # 获得焦点 对实例持续化响应


def inpu():  # 输入对话框
    def inp1():
        s = askstring('title', 'please input a string')
        # 还有askinteger askfloat 支持不同的类型
        labe1.config(text=s)

    btn1 = Button(root, text='弹出输入对话框', command=inp1)
    btn1.place(relx=0.2, rely=0.2)
    btn2 = Button(root, text='退出', command=root.destroy)
    btn2.place(relx=0.7, rely=0.2)


def fil1():  # 文件对话框
    def fil():
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            labe1.config(text='你选择的文件是' + filename)
            os.system(filename)
        else:
            labe1.config(text='你还未选择文件')

    btn1 = Button(root, text='弹出文件对话框', command=fil)
    btn1.place(relx=0.2, rely=0.2)
    btn2 = Button(root, text='退出', command=root.destroy)
    btn2.place(relx=0.7, rely=0.2)


def pho():  # 添加背景
    global photo  # 声明全局变量 防止被回收
    photo = Image.open('D://ps素材//鲸鱼.jpg')
    # photo = photo.resize((200, 200)) 这里先放弃控制大小
    photo = ImageTk.PhotoImage(photo)  # 使用其他库
    # photo = PhotoImage(file='D://py词云//小狗.gif')
    # 默认的photo_image 只能使用git格式 其他格式使用PIL
    p_label = Label(root, text='北冥有鱼\n其名为琨',
                    fg='white', font=('华文行楷', 25),
                    justify=LEFT,  # 对其方式
                    image=photo,
                    compound=CENTER)  # 字体显示位置
    p_label.pack()


def take():  # 打开摄像头
    def pri():
        btn.config(text='你真棒!')

    def video_loop():
        success, img = camera.read()  # 从摄像头读取照片
        if success:
            cv2.waitKey()
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
            imgtk = ImageTk.PhotoImage(image=current_image)
            panel.imgtk1 = imgtk
            panel.config(image=imgtk)
            root1.after(5000, video_loop)

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 设置摄像头
    root1 = Toplevel(root)  # 子窗口
    root1.geometry('300x300')
    root1.title('tk +  openCV')
    panel = Label(root1)
    panel.place(relwidth=1.0, relheight=0.8)
    btn = Button(root1, text='点赞', command=pri)
    btn.place(rely=0.8, relheight=0.1, relwidth=1.0)
    video_loop()
    camera.release()  # 关闭摄像头
    cv2.destroyAllWindows()  # 释放资源


def color():  # 颜色对话框
    def col():
        color_choose = tkinter.colorchooser.askcolor()
        colors = str(color_choose)  # 上面返回的是元组类型
        print(colors)
        labe1.config(text=colors[-9:-2], bg=colors[-9:-2])

    btn1 = Button(root, text='弹出颜色对话框', command=col)
    btn1.place(relx=0.2, rely=0.2)
    btn2 = Button(root, text='退出', command=root.destroy)
    btn2.place(relx=0.7, rely=0.2)


Main_menu = Menu(root)  # 实例一个菜单

Menu_file = Menu(Main_menu)  # 文件 菜单分组
Main_menu.add_cascade(label='文件', menu=Menu_file)  # 加一个菜单分组
Menu_file.add_command(label='新建', command=new)
Menu_file.add_command(label='打开', command=ope)
Menu_file.add_command(label='保存', command=sav)
Menu_file.add_separator()  # 分割线
Menu_file.add_command(label='退出', command=root.destroy)
# 退出

Menu_edit = Menu(Main_menu)  # 编辑 菜单分组
Main_menu.add_cascade(label='编辑', menu=Menu_edit)
Menu_edit.add_command(label='剪切', command=cut)
Menu_edit.add_command(label='复制', command=copy)
Menu_edit.add_command(label='粘贴', command=pas)

Menu_newroot = Menu(Main_menu)  # 新窗口 菜单分组
Main_menu.add_cascade(label='窗口', menu=Menu_newroot)
Menu_newroot.add_command(label='新建窗口', command=new_root)
Menu_newroot.add_command(label='按键测试', command=key_test)
Menu_newroot.add_command(label='添加背景', command=pho)
Menu_newroot.add_command(label='打开摄像头', command=take)

Menu_modal = Menu(Main_menu)  # 模式对话框 菜单分组
Main_menu.add_cascade(label='模式对话框', menu=Menu_modal)
Menu_modal.add_command(label='消息对话框', command=mess)
Menu_modal.add_command(label='输入对话框', command=inpu)
Menu_modal.add_command(label='文件对话框', command=fil1)
Menu_modal.add_command(label='颜色对话框', command=color)

root.config(menu=Main_menu)  # 将菜单实例化到root根窗体中
root.bind('<ButtonPress-3>', postmenu)  # 绑定鼠标右击事件
# 右键调用菜单实例 获得位置元组

root.mainloop()
