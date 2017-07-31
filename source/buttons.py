import tkinter
from source import windows
from source.settings import Settings


class UserChoiceButton(tkinter.Button):

    def __init__(self, master, column, row, data_type):
        super().__init__(master)

        self.data_type = data_type
        self.configure(
            font=Settings.current_settings['UserChoiceButton']['font'],
            state=Settings.current_settings['UserChoiceButton']['state'],
            cursor=Settings.current_settings['UserChoiceButton']['cursor'],
            overrelief=Settings.current_settings['UserChoiceButton']['overrelief'],
            background=Settings.current_settings['UserChoiceButton']['background'],
            foreground=Settings.current_settings['UserChoiceButton']['foreground'],
            borderwidth=Settings.current_settings['UserChoiceButton']['borderwidth'],
            highlightcolor=Settings.current_settings['UserChoiceButton']['highlightcolor'],
            activebackground=Settings.current_settings['UserChoiceButton']['activebackground'],
            activeforeground=Settings.current_settings['UserChoiceButton']['activeforeground'],
        )

        self['text'] = 'click'
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        windows.BasicInputWindow(self, data_type=self.data_type)

        # for future
        # os.startfile(path, 'open')
        # x = filedialog.askopenfilename(filetypes = (('.xls'), ('All files'))


class SettingsButton(tkinter.Button):

    def __init__(self, master, column, row):
        super().__init__(master)

        self.configure(
            font=Settings.current_settings['SettingsButton']['font'],
            state=Settings.current_settings['SettingsButton']['state'],
            cursor=Settings.current_settings['SettingsButton']['cursor'],
            overrelief=Settings.current_settings['SettingsButton']['overrelief'],
            background=Settings.current_settings['SettingsButton']['background'],
            foreground=Settings.current_settings['SettingsButton']['foreground'],
            borderwidth=Settings.current_settings['SettingsButton']['borderwidth'],
            highlightcolor=Settings.current_settings['SettingsButton']['highlightcolor'],
            activebackground=Settings.current_settings['SettingsButton']['activebackground'],
            activeforeground=Settings.current_settings['SettingsButton']['activeforeground'],
        )

        self['text'] = 'Settings'
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        windows.SettingsWindow(self)

        # Temporary debug.
        Settings.update()

        # self.update_idletasks()
        # print(self.winfo_y())
        # print(self.winfo_x())


class ColorButton(tkinter.Button):

    def __init__(self, master, column, row):
        super().__init__(master)

        self.configure(
            font=Settings.current_settings['ColorButton']['font'],
            state=Settings.current_settings['ColorButton']['state'],
            cursor=Settings.current_settings['ColorButton']['cursor'],
            overrelief=Settings.current_settings['ColorButton']['overrelief'],
            background=Settings.current_settings['ColorButton']['background'],
            foreground=Settings.current_settings['ColorButton']['foreground'],
            borderwidth=Settings.current_settings['ColorButton']['borderwidth'],
            highlightcolor=Settings.current_settings['ColorButton']['highlightcolor'],
            activebackground=Settings.current_settings['ColorButton']['activebackground'],
            activeforeground=Settings.current_settings['ColorButton']['activeforeground'],
        )

        self['text'] = 'Settings'
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=2, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        pass


class ViewButton(tkinter.Button):

    def __init__(self, master, column, row, text):
        super().__init__(master)

        self.configure(
            font=Settings.current_settings['ViewButton']['font'],
            state=Settings.current_settings['ViewButton']['state'],
            cursor=Settings.current_settings['ViewButton']['cursor'],
            overrelief=Settings.current_settings['ViewButton']['overrelief'],
            background=Settings.current_settings['ViewButton']['background'],
            foreground=Settings.current_settings['ViewButton']['foreground'],
            borderwidth=Settings.current_settings['ViewButton']['borderwidth'],
            highlightcolor=Settings.current_settings['ViewButton']['highlightcolor'],
            activebackground=Settings.current_settings['ViewButton']['activebackground'],
            activeforeground=Settings.current_settings['ViewButton']['activeforeground'],
        )

        self['text'] = text
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

        self.configure(
            font=Settings.current_settings['ApplyButton']['font'],
            state=Settings.current_settings['ApplyButton']['state'],
            cursor=Settings.current_settings['ApplyButton']['cursor'],
            overrelief=Settings.current_settings['ApplyButton']['overrelief'],
            background=Settings.current_settings['ApplyButton']['background'],
            foreground=Settings.current_settings['ApplyButton']['foreground'],
            borderwidth=Settings.current_settings['ApplyButton']['borderwidth'],
            highlightcolor=Settings.current_settings['ApplyButton']['highlightcolor'],
            activebackground=Settings.current_settings['ApplyButton']['activebackground'],
            activeforeground=Settings.current_settings['ApplyButton']['activeforeground'],
        )

        self['text'] = 'APPLY'
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

        self.configure(
            font=Settings.current_settings['CancelButton']['font'],
            state=Settings.current_settings['CancelButton']['state'],
            cursor=Settings.current_settings['CancelButton']['cursor'],
            overrelief=Settings.current_settings['CancelButton']['overrelief'],
            background=Settings.current_settings['CancelButton']['background'],
            foreground=Settings.current_settings['CancelButton']['foreground'],
            borderwidth=Settings.current_settings['CancelButton']['borderwidth'],
            highlightcolor=Settings.current_settings['CancelButton']['highlightcolor'],
            activebackground=Settings.current_settings['CancelButton']['activebackground'],
            activeforeground=Settings.current_settings['CancelButton']['activeforeground'],
        )

        self['text'] = 'CANCEL'
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

        self.configure(
            font=Settings.current_settings['OperationButton']['font'],
            state=Settings.current_settings['OperationButton']['state'],
            cursor=Settings.current_settings['OperationButton']['cursor'],
            overrelief=Settings.current_settings['OperationButton']['overrelief'],
            background=Settings.current_settings['OperationButton']['background'],
            foreground=Settings.current_settings['OperationButton']['foreground'],
            borderwidth=Settings.current_settings['OperationButton']['borderwidth'],
            highlightcolor=Settings.current_settings['OperationButton']['highlightcolor'],
            activebackground=Settings.current_settings['OperationButton']['activebackground'],
            activeforeground=Settings.current_settings['OperationButton']['activeforeground'],
        )

        self['text'] = 'click'
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

        self.configure(
            font=Settings.current_settings['DeleteButton']['font'],
            state=Settings.current_settings['DeleteButton']['state'],
            cursor=Settings.current_settings['DeleteButton']['cursor'],
            overrelief=Settings.current_settings['DeleteButton']['overrelief'],
            background=Settings.current_settings['DeleteButton']['background'],
            foreground=Settings.current_settings['DeleteButton']['foreground'],
            borderwidth=Settings.current_settings['DeleteButton']['borderwidth'],
            highlightcolor=Settings.current_settings['DeleteButton']['highlightcolor'],
            activebackground=Settings.current_settings['DeleteButton']['activebackground'],
            activeforeground=Settings.current_settings['DeleteButton']['activeforeground'],
        )

        self['text'] = 'click'
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

        self.configure(
            font=Settings.current_settings['AddButton']['font'],
            state=Settings.current_settings['AddButton']['state'],
            cursor=Settings.current_settings['AddButton']['cursor'],
            overrelief=Settings.current_settings['AddButton']['overrelief'],
            background=Settings.current_settings['AddButton']['background'],
            foreground=Settings.current_settings['AddButton']['foreground'],
            borderwidth=Settings.current_settings['AddButton']['borderwidth'],
            highlightcolor=Settings.current_settings['AddButton']['highlightcolor'],
            activebackground=Settings.current_settings['AddButton']['activebackground'],
            activeforeground=Settings.current_settings['AddButton']['activeforeground'],
        )

        self['text'] = 'click'
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

        self.configure(
            font=Settings.current_settings['OkayButton']['font'],
            state=Settings.current_settings['OkayButton']['state'],
            cursor=Settings.current_settings['OkayButton']['cursor'],
            overrelief=Settings.current_settings['OkayButton']['overrelief'],
            background=Settings.current_settings['OkayButton']['background'],
            foreground=Settings.current_settings['OkayButton']['foreground'],
            borderwidth=Settings.current_settings['OkayButton']['borderwidth'],
            highlightcolor=Settings.current_settings['OkayButton']['highlightcolor'],
            activebackground=Settings.current_settings['OkayButton']['activebackground'],
            activeforeground=Settings.current_settings['OkayButton']['activeforeground'],
        )

        self['text'] = 'click'
        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        pass
