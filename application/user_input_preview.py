import tkinter
import fields.database
import fields.template


class MainWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='slategray1')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='bottom', fill='x', expand='yes')
        for col_index in range(4):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(1):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        database = fields.database.DatabasePreview(self)
        database.enable(column=0, row=0)
        template = fields.template.TemplatePreview(self)
        template.enable(column=2, row=0)
