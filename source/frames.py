import tkinter

from source import fields, buttons


class MainFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='plum3')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='right', fill='x', expand='yes')

        # self.grid(column=1, row=0, columnspan=1, rowspan=1,
        #           padx=0, pady=0, ipadx=5, ipady=5,
        #           sticky='N' + 'S' + 'E' + 'W'
        # )

        # for col_index in range(2):
        #     self.columnconfigure(col_index, weight=1)
        # for row_index in range(2):
        #     self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        pass
        # console = fields.console.ConsoleField(self)
        # console.enable(column=0, row=0)


class FAQFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='right', fill='x', expand='yes')

        # self.grid(column=0, row=0, columnspan=1, rowspan=1,
        #           padx=0, pady=0, ipadx=5, ipady=5,
        #           sticky='N' + 'S' + 'E' + 'W'
        # )

        # for col_index in range(2):
        #     self.columnconfigure(col_index, weight=1)
        # for row_index in range(4):
        #     self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        faq = fields.FAQField(self)
        settings = buttons.SettingsButton(self)


class Operations(tkinter.Frame):
    pass