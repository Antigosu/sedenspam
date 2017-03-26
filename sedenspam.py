import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('sedenspam')
        self.size = '600x300'
        self.geometry(f'{self.size}+300+225')
        self.wm_iconbitmap('.\images\sedenspam.ico')
        self.configure(background='thistle4')
        self.center_application()
        self.create_windows()

    def create_windows(self):
        MainWindow(self)

    def center_application(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 300 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2
        self.geometry(f'{self.size}+{x}+{y}')


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        faq = FAQField(self)
        faq.enable(column=0, row=1)
        email = PathButton(self)
        email.enable(column=0 ,row=2)
        template = PathButton(self)
        template.enable(column=0, row=3)
        database = PathButton(self)
        database.enable(column=0, row=4)
        email_status = StatusLabel(self)
        email_status.enable(column=1, row=2)
        template_status = StatusLabel(self)
        template_status.enable(column=1, row=3)
        database_status = StatusLabel(self)
        database_status.enable(column=1, row=4)


class DialogWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.size = '200x150'
        self.master = master
        self.slave = tk.Toplevel(master)
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


class FAQField(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Добро пожаловать в SED-EN-SPAM!!1\n' \
                       'Рассылка спама теперь еще веселее и продуктивнее.'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['relief'] = 'raised',
        self['borderwidth'] = 1

    def enable(self, column, row):
        self.grid(
            column=column,
            row=row,
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
        self['command'] = self.click

    def enable(self, column, row):
        self.grid(
            column=column,
            row=row,
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

    def click(self):
        DialogWindow(self)

class StatusLabel(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'V'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['relief'] = 'raised',
        self['borderwidth'] = 1

    def enable(self, column, row):
        self.grid(
            column=column,
            row=row,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='N' + 'S' + 'E' + 'W'
        )


# TODO: main block
root = Application()
root.mainloop()
