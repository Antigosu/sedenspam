import tkinter


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
