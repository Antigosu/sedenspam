import tkinter
import source.windows


class PathButton(tkinter.Button):
    def __init__(self, master):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=1,
    #         rowspan=1,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )
    #
    # def disable(self):
    #     self.grid_forget()

    def click(self):
        source.windows.DialogWindow(self)


class SettingsButton(tkinter.Button):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'sets'
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=1,
    #         rowspan=1,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )
    #
    # def disable(self):
    #     self.grid_forget()

    def click(self):
        source.windows.DialogWindow(self)


class YesNoButton(tkinter.Button):
    pass