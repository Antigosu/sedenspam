import tkinter
from source import labels, buttons


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='cyan3')
        self.columnconfigure(0, weight=1, minsize=350)
        self.columnconfigure(1, weight=1, minsize=65)
        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=65)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        labels.FAQLabel(self)
        buttons.SettingsButton(self)

        labels.StatusLabel(self, 1)
        buttons.PathButton(self, 1)

        labels.StatusLabel(self, 2)
        buttons.PathButton(self, 2)

        labels.StatusLabel(self, 3)
        buttons.PathButton(self, 3)


class OperationFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')
        for col_index in range(2):
            self.rowconfigure(col_index, weight=1, minsize=100)
        for row_index in range(2):
            self.rowconfigure(row_index, weight=1, minsize=65)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        labels.ConsoleLabel(self)
        buttons.OperationButton(self, column=0, row=1)
        buttons.OperationButton(self, column=1, row=1)