import tkinter
import fields.console


class MainWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='plum3')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        self.pack(side='right', fill='both', expand='yes')
        for col_index in range(2):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(2):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        console = fields.console.ConsoleField(self)
        console.enable(column=0, row=0)
