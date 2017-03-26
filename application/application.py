import tkinter
import windows.main


class Application(tkinter.Tk):
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
        windows.main.MainWindow(self)

    def center_application(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # size = tuple(int(number) for number in self.geometry().split('+')[0].split('x'))
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 300 / 2)
        # x = w / 2 - size[0] / 2
        # y = h / 2 - size[1] / 2
        self.geometry(f'{self.size}+{x}+{y}')
