import tkinter
from source import windows, settings


class UserChoiceButton(tkinter.Button):

    def __init__(self, master, column, row, data_type):
        super().__init__(master)

        self.data_type = data_type
        self['text'] = 'click'
        self['command'] = self.click
        self.configure(
            foreground=settings.Settings.current_settings['UserChoiceButton']['foreground'],
            background=settings.Settings.current_settings['UserChoiceButton']['background'],
            borderwidth=settings.Settings.current_settings['UserChoiceButton']['borderwidth'],
            font=settings.Settings.current_settings['UserChoiceButton']['font'],
            state=settings.Settings.current_settings['UserChoiceButton']['state'],
            cursor=settings.Settings.current_settings['UserChoiceButton']['cursor'],
            activeforeground=settings.Settings.current_settings['UserChoiceButton']['activeforeground'],
            activebackground=settings.Settings.current_settings['UserChoiceButton']['activebackground'],
            highlightcolor=settings.Settings.current_settings['UserChoiceButton']['highlightcolor'],
            overrelief=settings.Settings.current_settings['UserChoiceButton']['overrelief']
        )


        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        windows.BasicInputWindow(self, data_type=self.data_type)

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

        self['text'] = 'Settings'
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

        windows.SettingsWindow(self)

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
        self['relief'] = 'raised'
        self['borderwidth'] = 3

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        self.master.color = self['bg']


class ViewButton(tkinter.Button):

    def __init__(self, master, column, row, text):
        super().__init__(master)

        self['text'] = text
        self['fg'] = 'black',
        self['bg'] = 'skyblue',
        self['cursor'] = 'pirate',
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        self.master.view = self['text']


class ApplyButton(tkinter.Button):

    def __init__(self, master, column, row):
        super().__init__(master)

        self['text'] = 'APPLY'
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.apply

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def apply(self):
        self.master.apply()


class CancelButton(tkinter.Button):

    def __init__(self, master, column, row):
        super().__init__(master)

        self['text'] = 'CANCEL'
        self['fg'] = 'black',
        self['bg'] = 'tan1',
        self['cursor'] = 'pirate',
        self['command'] = self.cancel

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def cancel(self):
        self.master.cancel()


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
