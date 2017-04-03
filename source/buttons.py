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

        # for col_index in range(2):
        #     self.columnconfigure(col_index, weight=1)
        # for row_index in range(4):
        #     self.rowconfigure(row_index, weight=1)

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
        self.pack(side='top')
        # self.pack(side='top', fill='x', expand='yes')

    def click(self):
        source.windows.DialogWindow(self)


class YesNoButton(tkinter.Button):
    pass
