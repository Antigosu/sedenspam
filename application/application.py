import tkinter

import application.user_input


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('sedenspam')
        self.x = '600'
        self.y = '300'
        self.geometry(f'{self.x}x{self.y}+300+225')
        self.wm_iconbitmap('.\images\sedenspam.ico')
        self.configure(background='thistle4')
        self.center_application()
        self.create_windows()

    def create_windows(self):
        application.user_input.MainWindow(self)

    def center_application(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 300 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2
        self.geometry(f'{self.x}x{self.y}+{x}+{y}')
