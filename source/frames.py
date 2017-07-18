import tkinter
from source import labels, buttons


class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')  # Different colors for debug.

        # for col_index in range(5):
        #     self.columnconfigure(col_index, weight=1, minsize=150)
        # self.rowconfigure(0, weight=1, minsize=75)

        self.pack(side='top', fill='both', expand='yes')

        self.setupFrame = SetupFrame(self)
        self.operationFrame = OperationFrame(self)


class PreviewFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')  # Different colors for debug.

        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=300)
        self.rowconfigure(0, weight=1, minsize=300)

        self.pack(side='top', fill='both', expand='yes')

        self.templatePreview = labels.PreviewLabel(master=self, column=0, row=0)
        self.emailPreview = labels.PreviewLabel(master=self, column=1, row=0)


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='cyan3')  # Different colors for debug.
        self.columnconfigure(0, weight=1, minsize=225)
        self.columnconfigure(1, weight=1, minsize=75)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='left', fill='both', expand='yes')

        self.faqLabel = labels.FAQLabel(master=self, column=0, row=0)
        self.emailLabel = labels.UserChoiceLabel(master=self, column=0, row=1)
        self.templateLabel = labels.UserChoiceLabel(master=self, column=0, row=2)
        self.databaseLabel = labels.UserChoiceLabel(master=self, column=0, row=3)

        self.settingsButton = buttons.SettingsButton(master=self, column=1, row=0)
        self.emailButton = buttons.UserChoiceButton(master=self, column=1, row=1)
        self.templateButton = buttons.UserChoiceButton(master=self, column=1, row=2)
        self.databaseButton = buttons.UserChoiceButton(master=self, column=1, row=3)


class OperationFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')  # Different colors for debug.
        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='right', fill='both', expand='yes')

        self.console = labels.ConsoleLabel(master=self, column=0, row=0)

        self.sendButton = buttons.OperationButton(master=self, column=0, row=2)
        self.exitButton = buttons.OperationButton(master=self, column=1, row=2)


class SettingsFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')  # Different colors for debug.

        for col_index in range(6):
            self.columnconfigure(col_index, weight=1, minsize=150)

        for row_index in range(6):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='left', fill='both', expand='yes')

        self.colorLabel = labels.SettingsLabel(master=self, column=0, row=0)
        self.viewLabel = labels.SettingsLabel(master=self, column=0, row=2)
        self.confirmLabel = labels.SettingsLabel(master=self, column=0, row=4)

        self.colorButton1 = buttons.ColorButton(master=self, column=0, row=1)
        self.colorButton2 = buttons.ColorButton(master=self, column=1, row=1)
        self.colorButton3 = buttons.ColorButton(master=self, column=2, row=1)

        self.viewButton1 = buttons.ViewButton(master=self, column=0, row=3)
        self.viewButton2 = buttons.ViewButton(master=self, column=1, row=3)
        self.viewButton3 = buttons.ViewButton(master=self, column=2, row=3)

        self.confirmButton1 = buttons.ConfirmButton(master=self, column=0, row=5)
        self.confirmButton2 = buttons.ConfirmButton(master=self, column=1, row=5)
        self.confirmButton3 = buttons.ConfirmButton(master=self, column=2, row=5)
