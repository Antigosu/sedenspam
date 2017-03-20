import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('sedenspam')
        self.geometry('600x300+300+225')
        self.wm_iconbitmap('.\images\sedenspam.ico')
        self.configure(background='thistle4')
        MainWindow(self)


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        FAQField(self)


class DialogWindow:
    def __init__(self, master):
        self.slave = tk.Toplevel(master)
        self.slave.title('sedenspam')
        self.slave.geometry('200x150+500+375')


class FAQField(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Добро пожаловать в SED-EN-SPAM!!1\n' \
                       'Рассылка спама теперь еще веселее и продуктивнее.'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['relief'] = 'raised',
        self['borderwidth'] = 1
        self.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

# TODO: main block
root = Application()
root.mainloop()
