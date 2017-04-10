import tkinter
from source import labels, buttons


class SetupFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='cyan3')
        self.columnconfigure(0, weight=1, minsize=225)
        self.columnconfigure(1, weight=1, minsize=75)
        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.pack(side='left', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        # TODO: think about pep
        faq_label = labels.FAQLabel(self)
        settings_button = buttons.SettingsButton(self)

        email_choice_label = labels.UserChoiceLabel(self, 1)
        email_choice_button = buttons.UserChoiceButton(self, 1)

        template_choice_label = labels.UserChoiceLabel(self, 2)
        template_choice_button = buttons.UserChoiceButton(self, 2)

        database_choice_label = labels.UserChoiceLabel(self, 3)
        database_choice_button = buttons.UserChoiceButton(self, 3)


class ConsoleFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')
        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)
        self.rowconfigure(0, weight=1, minsize=75)
        self.rowconfigure(1, weight=1, minsize=75)

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

        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=300)
        self.rowconfigure(0, weight=1, minsize=300)

        self.pack(side='top', fill='both', expand='yes')
        self.create_widgets()

    def create_widgets(self):
        labels.PreviewLabel(self, column=0)
        labels.PreviewLabel(self, column=1)
