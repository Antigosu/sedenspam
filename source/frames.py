import tkinter
from source import labels, buttons


# maybe useless
class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='plum3')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        # self.master.geometry('600x600+300+225')
        self.create_widgets()
        self.pack(side='right', fill='both', expand='yes')

        for col_index in range(1):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(1):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        InputFrame(self)


class TextFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='cyan3')
        # self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        # self.master.geometry('600x600+300+225')
        self.create_widgets()
        # self.pack(side='top')
        self.pack(side='left', fill='none', expand='yes')

        for col_index in range(1):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(4):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        labels.FAQLabel(self)
        l1 = labels.StatusLabel(self, 1)
        l2 = labels.StatusLabel(self, 2)
        l3 = labels.StatusLabel(self, 3)

class ButtonsFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='sienna1')
        # self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        # self.master.geometry('600x600+300+225')
        self.create_widgets()
        # self.pack(side='top')
        self.pack(side='top', fill='both', expand='yes')

        for col_index in range(2):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(1):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        buttons.SettingsButton(self)
        p1 = buttons.PathButton(self, 1)
        p2 = buttons.PathButton(self, 2)
        p3 = buttons.PathButton(self, 3)

class InputFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        # self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        # self.master.geometry('600x600+300+225')
        self.create_widgets()
        # self.pack(side='top')
        self.pack(side='top', fill='none', expand='yes')

        for col_index in range(2):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(3):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        TextFrame(self)
        ButtonsFrame(self)


class Operations(tkinter.Frame):
    pass
