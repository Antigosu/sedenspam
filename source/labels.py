import tkinter


class FAQLabel(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Добро пожаловать в SED-EN-SPAM!!1\n' \
                       'Рассылка спама теперь еще веселее и продуктивнее.'
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=0,
            row=0,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='WENS'
        )


class UserChoiceLabel(tkinter.Label):
    def __init__(self, master, row):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'tan1'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=0,
            row=row,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass


class ConsoleLabel(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'skyblue'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=0,
            row=0,
            columnspan=2,
            rowspan=2,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass


class PreviewLabel(tkinter.Label):
    def __init__(self, master, column):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'skyblue'
        self['relief'] = 'raised'
        self['borderwidth'] = 1

        self.grid(
            column=column,
            row=0,
            columnspan=1,
            rowspan=1,
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
            sticky='WENS'
        )

    def change_status(self):
        pass
