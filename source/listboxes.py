import tkinter


class BasicListbox(tkinter.Listbox):

    def __init__(self, master, column, row, data_type):
        super().__init__(master)

        self.data_type = data_type

        self.configure(font=["Fira Code", "15", "bold"],
                       foreground='#455a64',
                       background='#cfd8dc')

        # Temporary, just for debug.
        self.email_list = [
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru',
            'avorochalkin@en-pro.ru'
        ]

        # Temporary, just for debug.
        self.template_list = [
            'sedmax_template_1',
            'sedmax_template_2',
            'sedmax_template_3',
            'sedmax_template_4',
            'sedmax_template_5'
        ]

        # Temporary, just for debug.
        self.database_list = [
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
            for email in self.email_list:
                self.insert('end', email)

        elif self.data_type == 'template':
            for template in self.template_list:
                self.insert('end', template)

        elif self.data_type == 'database':
            for database in self.database_list:
                self.insert('end', database)
