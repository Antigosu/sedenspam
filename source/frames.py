import tkinter
from source import fields, buttons


class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='plum3')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='right', fill='x', expand='yes')

    def create_widgets(self):
        pass


class FAQFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='right', fill='x', expand='yes')

    def create_widgets(self):
        fields.FAQField(self)
        buttons.SettingsButton(self)


class Operations(tkinter.Frame):
    pass
