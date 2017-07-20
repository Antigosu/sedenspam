import tkinter


class EmailListbox(tkinter.Listbox):
    def __init__(self, master, column, row):
        super().__init__(master)

        self.emailList = [
            # temporary for debug
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
        ]

        self.grid(
            column=column, row=row, columnspan=3, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

        for email in self.emailList:
            self.insert('end', email)

