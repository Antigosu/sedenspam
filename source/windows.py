import tkinter

from source import frames


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('sedenspam')
        self.x = '600'
        self.y = '600'
        self.geometry(f'{self.x}x{self.y}+300+225')
        self.wm_iconbitmap('..\images\sedenspam.ico')
        self.configure(background='thistle4')
        self.center_application()
        self.create_windows()

    def create_windows(self):
        faq = frames.FAQFrame(self)

    def center_application(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 600 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2
        self.geometry(f'{self.x}x{self.y}+{x}+{y}')


class Email(tkinter.Tk):
    pass


class DialogWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.size = '200x150'
        self.master = master
        self.slave = tkinter.Toplevel(master)
        self.slave.title('sedenspam')
        # self.slave.geometry(f'{self.size}+500+375')
        self.center_window()

    def center_window(self):
        self.master.update_idletasks()
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(w / 2 - 200 / 2)
        y = int(h / 2 - 150 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2
        self.slave.geometry(f'{self.size}+{x}+{y}')


class Settings(tkinter.Tk):
    pass


class YesNo(tkinter.Tk):
    pass
