import tkinter
from source import labels, buttons


class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')      # Different colors for debug.

        # for col_index in range(5):
        #     self.columnconfigure(col_index, weight=1, minsize=150)
        # self.rowconfigure(0, weight=1, minsize=75)

        self.pack(side='top', fill='both', expand='yes')

        self.setupFrame = SetupFrame(self)
        self.consoleFrame = ConsoleFrame(self)
        self.operationFrame = OperationFrame(self)


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='cyan3')      # Different colors for debug.
        self.columnconfigure(0, weight=1, minsize=225)
        self.columnconfigure(1, weight=1, minsize=75)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='left', fill='both', expand='yes')

        self.faqInfo = labels.FAQLabel(master=self, column=0, row=0)
        self.emailInfo = labels.UserChoiceLabel(master=self, column=0, row=1)
        self.templateInfo = labels.UserChoiceLabel(master=self, column=0, row=2)
        self.databaseInfo = labels.UserChoiceLabel(master=self, column=0, row=3)

        self.settings = buttons.SettingsButton(master=self, column=1, row=0)
        self.email = buttons.UserChoiceButton(master=self, column=1, row=1)
        self.template = buttons.UserChoiceButton(master=self, column=1, row=2)
        self.database = buttons.UserChoiceButton(master=self, column=1, row=3)


class ConsoleFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')      # Different colors for debug.
        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)
        self.rowconfigure(0, weight=1, minsize=75)
        self.rowconfigure(1, weight=1, minsize=75)

        self.pack(side='top', fill='both', expand='yes')

        self.console = labels.ConsoleLabel(master=self, column=0, row=0)


class OperationFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')        # Different colors for debug.
        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)

        for row_index in range(2):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='right', fill='both', expand='yes')

        self.send = buttons.OperationButton(master=self, column=0, row=0)
        self.exit = buttons.OperationButton(master=self, column=1, row=0)


class PreviewFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')      # Different colors for debug.

        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=300)
        self.rowconfigure(0, weight=1, minsize=300)

        self.pack(side='top', fill='both', expand='yes')

        self.templatePreview = labels.PreviewLabel(master=self, column=0, row=0)
        self.emailPreview = labels.PreviewLabel(master=self, column=1, row=0)
