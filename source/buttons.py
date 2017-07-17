import tkinter
import source.windows


class UserChoiceButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'click',
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1, # 1 - x
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.DialogWindow(self)
        self.update_idletasks() # Temporary debug.
        print(self.winfo_y())
        print(self.winfo_x())


class SettingsButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'sets'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1, # 1 - 0
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.DialogWindow(self)
        self.update_idletasks() # Temporary debug.
        print(self.winfo_y())
        print(self.winfo_x())


class OperationButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'springgreen3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=2, # x - 0
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.DialogWindow(self)
        self.update_idletasks()  # Temporary debug.
        print(self.winfo_y())
        print(self.winfo_x())

class YesNoButton(tkinter.Button):
    pass
