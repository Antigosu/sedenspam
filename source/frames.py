import tkinter
from source import labels, buttons


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='cyan3')
        self.columnconfigure(0, weight=1, minsize=350)
        self.columnconfigure(1, weight=1, minsize=65)
        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='left', fill='both', expand='yes')
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


class ConsoleFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')
        self.columnconfigure(0, weight=1, minsize=310)
        self.rowconfigure(0, weight=1, minsize=75)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        labels.ConsoleLabel(self)


class OperationFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')
        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)
        for row_index in range(2):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='right', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        buttons.OperationButton(self, column=0)
        buttons.OperationButton(self, column=1)


class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')

        # for col_index in range(5):
        #     self.columnconfigure(col_index, weight=1, minsize=150)
        # self.rowconfigure(0, weight=1, minsize=75)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        SetupFrame(self)
        ConsoleFrame(self)
        OperationFrame(self)


class PreviewFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')

        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)
        self.rowconfigure(0, weight=1, minsize=245)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        labels.PreviewLabel(self, column=0)
        labels.PreviewLabel(self, column=1)
