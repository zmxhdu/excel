# coding = utf-8

import tkinter
import tkinter.messagebox
import MainPage


# # 创建应用程序窗口
# root = tkinter.Tk()
# root.geometry('200x150')
# varName = tkinter.StringVar()
# varName.set('')
# varPwd = tkinter.StringVar()
# varPwd.set('')

# 创建标签
labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, width=80)
labelPwd = tkinter.Label(root, text='User Pwd:', justify=tkinter.RIGHT, width=80)

# 将标签放到窗口上
labelName.place(x=10, y=5, width=80, height=20)
labelPwd.place(x=10, y=30, width=80, height=20)

# 创建文本框，同时设置关联的变量
entryName = tkinter.Entry(root, width=80, textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

entryPwd = tkinter.Entry(root, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)


# 登录按钮事件处理函数
def login():
    name = entryName.get()
    pwd = entryPwd.get()
    if name == 'admin' and pwd == '123456':
        tkinter.messagebox.showinfo(title='Python tkinter', message='OK')
    else:
        tkinter.messagebox.showerror(title='Python tkinter', message='Error')


buttonLogin = tkinter.Button(root, text='Login', command=login)
buttonLogin.place(x=30, y=120, width=50, height=20)


def cancel():
    varName.set('')
    varPwd.set('')


buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=130, y=120, width=50, height=20)


class Login(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (200,150))  # 设置窗口大小
        self.root.resizable(False, False)
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.createPage()

    def createPage(self):

