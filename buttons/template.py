import tkinter
from windows.path import DialogWindow


class PathButton(tkinter.Button):
    def __init__(self, master):
        super().__init__(master)
        self.path = 'Укажите путь до файла...'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click

    def enable(self, column, row):
        self.grid(
            column=column,
            row=row,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='N' + 'S' + 'E' + 'W'
        )

    def disable(self):
        self.grid_forget()

    def click(self):
        DialogWindow(self)
