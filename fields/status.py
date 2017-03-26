import tkinter


class StatusLabel(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'V'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['relief'] = 'raised',
        self['borderwidth'] = 1

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

    def change_status(self):
        pass
