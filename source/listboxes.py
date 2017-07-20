import tkinter


class BasicListbox(tkinter.Listbox):
    def __init__(self, master, column, row, data_type):
        super().__init__(master)
        self.data_type = data_type
        self.emailList = [
            # Temporary, just for debug.
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru'
        ]
        self.templateList = [
            # Temporary, just for debug.
            'sedmax_template_1',
            'sedmax_template_2',
            'sedmax_template_3',
            'sedmax_template_4',
            'sedmax_template_5'
        ]
        self.databaseList = [
            # Temporary, just for debug.
            'Vologda',
            'Novocherkassk',
            'Moscow',
            'Ufa',
            'London is a capital of GB'
        ]

        self.grid(
            column=column, row=row, columnspan=3, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

        # Temporary, just for debug.
        if self.data_type == 'email':
            for email in self.emailList:
                self.insert('end', email)
        elif self.data_type == 'template':
            for template in self.templateList:
                self.insert('end', template)
        elif self.data_type == 'database':
            for database in self.databaseList:
                self.insert('end', database)
