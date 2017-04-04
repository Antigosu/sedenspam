import tkinter
from source import labels, buttons


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='cyan3')
        # self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        # self.master.geometry('600x600+300+225')
        self.create_widgets()
        self.pack(side='top', fill='both', expand='yes')

        self.columnconfigure(0, weight=1, minsize=350)
        self.columnconfigure(1, weight=1, minsize=65)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=65)

    def create_widgets(self):
        labels.FAQLabel(self)
        buttons.SettingsButton(self)

        labels.StatusLabel(self, 1)
        buttons.PathButton(self, 1)

        labels.StatusLabel(self, 2)
        buttons.PathButton(self, 2)

        labels.StatusLabel(self, 3)
        buttons.PathButton(self, 3)

class Operations(tkinter.Frame):
    pass
