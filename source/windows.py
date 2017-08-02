import tkinter
from source import frames, settings


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.settings = settings.Settings()

        self.title('sedenspam')
        self.x = '100'
        self.y = '100'
        self.geometry(f'{self.x}x{self.y}+300+225')
        self.wm_iconbitmap('..\images\sedenspam.ico')
        self.configure(background='thistle4')
        self.minsize(width=800, height=600)
        self.center_application()

        self.mainFrame = frames.MainFrame(self)
        self.previewFrame = frames.PreviewFrame(self)

    def center_application(self):

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 600 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2

        self.geometry(f'{self.x}x{self.y}+{x}+{y}')


class SettingsWindow(tkinter.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.size = '300x300'
        self.resizable(0, 0)
        # self.master = master
        self.title('Settings')
        # self.geometry(f'{self.size}+500+375')
        self.wm_iconbitmap('..\images\sedenspam.ico')
        self.center_window()

        self.settingsFrame = frames.SettingsFrame(self)

        # self.focus_set()
        self.grab_set()

    def center_window(self):

        self.master.update_idletasks()

        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()

        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(w / 2 - 200 / 2)
        y = int(h / 2 - 150 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2

        self.geometry(f'{self.size}+{x}+{y}')


class BasicInputWindow(tkinter.Toplevel):

    def __init__(self, master, data_type):
        super().__init__(master)

        self.data_type = data_type

        self.size = '450x300'
        # self.master = master
        self.title(f'Basic {self.data_type} information')
        # self.geometry(f'{self.size}+500+375')
        self.wm_iconbitmap('..\images\sedenspam.ico')
        self.center_window()

        if self.data_type == 'email':
            self.email_frame = frames.BasicInputFrame(self, data_type)
        elif self.data_type == 'template':
            self.template_frame = frames.BasicInputFrame(self, data_type)
        elif self.data_type == 'database':
            self.database_frame = frames.BasicInputFrame(self, data_type)

    def center_window(self):

        self.master.update_idletasks()

        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()

        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(w / 2 - 200 / 2)
        y = int(h / 2 - 150 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2

        self.geometry(f'{self.size}+{x}+{y}')


class YesNo(tkinter.Tk):

    pass
