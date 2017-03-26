import tkinter


class ConsoleField(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.event = 'Сейчас что-то происходит...'
        self['text'] = self.event,
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['relief'] = 'raised',
        self['borderwidth'] = 1

    def enable(self, column, row):
        self.grid(
            column=column,
            row=row,
            columnspan=1,
            rowspan=2,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='N' + 'S' + 'E' + 'W'
        )
