import tkinter
import source.windows  # Just for now, uncomment after debug.


class UserChoiceButton(tkinter.Button):
    def __init__(self, master, column, row, data_type):
        super().__init__(master)
        self.data_type = data_type
        self['text'] = 'click',
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        source.windows.BasicInputWindow(self, data_type=self.data_type)


        # Temporary debug.

        # self.update_idletasks()
        # print(self.winfo_y())
        # print(self.winfo_x())

        # for future
        # os.startfile(path, 'open')
        # x = filedialog.askopenfilename(filetypes = (('.xls'), ('All files'))

class SettingsButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'sets'
        self['fg'] = 'black',
        self['bg'] = 'bisque3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        source.windows.SettingsWindow(self)

        # Temporary debug.

        # self.update_idletasks()
        # print(self.winfo_y())
        # print(self.winfo_x())


class ColorButton(tkinter.Button):
    def __init__(self, master, column, row, color):
        super().__init__(master)
        self['fg'] = 'black',
        self['bg'] = color,
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.SettingsWindow(self)

        # Temporary debug.

        self.update_idletasks()
        print(self.winfo_y())
        print(self.winfo_x())


class ViewButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'sets'
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.SettingsWindow(self)

        # Temporary debug.

        self.update_idletasks()
        print(self.winfo_y())
        print(self.winfo_x())


class ConfirmButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self['text'] = 'sets'
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.SettingsWindow(self)

        # Temporary debug.

        self.update_idletasks()
        print(self.winfo_y())
        print(self.winfo_x())


class OperationButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'springgreen3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=3,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        # source.windows.SettingsWindow(self)

        # Temporary debug.

        self.update_idletasks()
        print(self.winfo_y())
        print(self.winfo_x())


class DeleteButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'springgreen3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        pass


class AddButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'springgreen3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        pass


class OkayButton(tkinter.Button):
    def __init__(self, master, column, row):
        super().__init__(master)
        self.path = 'click'
        self['text'] = self.path,
        self['fg'] = 'black',
        self['bg'] = 'springgreen3',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):
        pass
