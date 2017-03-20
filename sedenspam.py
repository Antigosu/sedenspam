import tkinter as tk


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('sedenspam')
        self.master.geometry('600x300+300+225')

        DialogWindow(self.master)
        self.master.mainloop()


class DialogWindow:
    def __init__(self, master):
        self.slave = tk.Toplevel(master)
        self.slave.title('sedenspam')
        self.slave.geometry('200x150+500+375')


root = tk.Tk()
MainWindow(root)