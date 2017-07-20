import tkinter


class FAQLabel(tkinter.Label):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'welcome'
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )


class UserChoiceLabel(tkinter.Label):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'tan1'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass


class ConsoleLabel(tkinter.Label):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'skyblue'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column, row=row, columnspan=2, rowspan=2,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass


class PreviewLabel(tkinter.Label):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'skyblue'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass


class SettingsLabel(tkinter.Label):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'Choose your prefer color and view settings'
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column, row=row, columnspan=3, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )
