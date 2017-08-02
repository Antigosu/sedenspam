import tkinter


class FAQLabel(tkinter.Label):

    def __init__(self, master, column, row):
        super().__init__(master)

        self['text'] = 'welcome to SES v.0\nfor latest updates please check out \nhttps://github.com/antigosu/sedenspam'
        self['fg'] = '#ffffff'
        self['bg'] = '#FF5370'
        self['relief'] = 'raised'
        self['borderwidth'] = 2

        self.configure(font=["Fira Code", "10", "bold"])

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
        self['fg'] = '#cfd8dc'
        self['bg'] = '#607d8b'
        self['relief'] = 'raised'
        self['borderwidth'] = 2

        self.configure(font=["Fira Code", "15", "bold"])

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
        self['fg'] = '#cfd8dc'
        self['bg'] = '#757575'
        self['relief'] = 'raised'
        self['borderwidth'] = 2

        self.configure(font=["Fira Code", "10", "bold"])

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
        self['fg'] = '#cfd8dc'
        self['bg'] = '#757575'
        self['relief'] = 'raised'
        self['borderwidth'] = 2

        self.configure(font=["Fira Code", "10", "bold"])

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
        self['fg'] = '#ffffff'
        self['bg'] = '#FF5370'
        self['relief'] = 'raised'
        self['borderwidth'] = 2

        self.configure(font=["Fira Code", "10", "bold"])

        self.grid(
            column=column, row=row, columnspan=2, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )
