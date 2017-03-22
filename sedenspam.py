import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('sedenspam')
        self.geometry('600x300+300+225')
        self.wm_iconbitmap('.\images\sedenspam.ico')
        self.configure(background='thistle4')
        self.createWindows()

    def createWindows(self):
        MainWindow(self)


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.createWidgets()
        self.grid()

    def createWidgets(self):
        faq = FAQField(self).enable(row=1)
        email = PathButton(self).enable(row=2)
        template = PathButton(self).enable(row=3)
        database = PathButton(self).enable(row=4)


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

    def enable(self, row):
        self.grid(
            row=row,
            column=0,
            columnspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='N' + 'S' + 'E' + 'W'
        )

    def disable(self):
        self.grid_forget()


class PathButton(tk.Button):
    def __init__(self, master):
        super().__init__(master)
        self.path = 'Укажите путь до файла...'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        # self['command'] = self.click()

    def enable(self, row):
        self.grid(
            row=row,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='N' + 'S' + 'E' + 'W'
        )

    def disable(self):
        self.grid_forget()

    # def click(self):
    #     DialogWindow(self)


# TODO: main block
root = Application()
root.mainloop()
