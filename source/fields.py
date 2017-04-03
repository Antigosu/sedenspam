import tkinter


class ConsoleField(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = 'Сейчас что-то происходит...'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=2,
    #         rowspan=2,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )


class DatabasePreview(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = '\n\n\nЗагружаем базу данных...\n\n\n'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=2,
    #         rowspan=1,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )


class FAQField(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Добро пожаловать в SED-EN-SPAM!!1\n' \
                       'Рассылка спама теперь еще веселее и продуктивнее.'
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=1,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )
    #
    # def disable(self):
    #     self.grid_forget()


class StatusLabel(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
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

    def change_status(self):
        pass


class TemplatePreview(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = '\n\n\nЗагружаем структуру письма...\n\n\n'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')

    # def enable(self, column, row):
    #     self.grid(
    #         column=column,
    #         row=row,
    #         columnspan=2,
    #         rowspan=1,
    #         padx=5,
    #         pady=5,
    #         ipadx=5,
    #         ipady=5,
    #         sticky='N' + 'S' + 'E' + 'W'
    #     )
