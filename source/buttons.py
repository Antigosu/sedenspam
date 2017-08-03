import tkinter
from source import windows
from source.settings import Settings


class UserChoiceButton(tkinter.Button):

    def __init__(self, master, column, row, data_type):
        super().__init__(master)

        self.data_type = data_type
        self.configure(
            font=Settings.current_settings['UserChoiceButton']['font'],
            state=Settings.current_settings['UserChoiceButton']['state'][Settings.theme],
            cursor=Settings.current_settings['UserChoiceButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['UserChoiceButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['UserChoiceButton']['background'][Settings.theme],
            foreground=Settings.current_settings['UserChoiceButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['UserChoiceButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['UserChoiceButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['UserChoiceButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['UserChoiceButton']['activeforeground'][Settings.theme]
        )

        self['command'] = self.click

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

        self.image1 = tkinter.PhotoImage(file=r'..\images\user-lightgrey.png')
        self.image2 = tkinter.PhotoImage(file=r'..\images\form-lightgrey.png')
        self.image3 = tkinter.PhotoImage(file=r'..\images\base-lightgrey.png')
        if self.data_type == 'email':
            self['image'] = self.image1
            self['text'] = ' user'
        elif self.data_type == 'template':
            self['image'] = self.image2
            self['text'] = ' form'
        elif self.data_type == 'database':
            self['image'] = self.image3
            self['text'] = ' base'

        self['compound'] = 'left'

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
            state=Settings.current_settings['SettingsButton']['state'][Settings.theme],
            cursor=Settings.current_settings['SettingsButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['SettingsButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['SettingsButton']['background'][Settings.theme],
            foreground=Settings.current_settings['SettingsButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['SettingsButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['SettingsButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['SettingsButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['SettingsButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' tune'
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\tune-white.png')
        self['image'] = self.image
        self['compound'] = 'left'

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        windows.SettingsWindow(self)

        # Temporary debug.
        # Settings.update()
        #
        # self.update_idletasks()
        # print(self.winfo_y())
        # print(self.winfo_x())


class ColorButton(tkinter.Button):

    def __init__(self, master, column, row):
        super().__init__(master)

        self.configure(
            font=Settings.current_settings['ColorButton']['font'],
            state=Settings.current_settings['ColorButton']['state'][Settings.theme],
            cursor=Settings.current_settings['ColorButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['ColorButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['ColorButton']['background'][Settings.theme],
            foreground=Settings.current_settings['ColorButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['ColorButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['ColorButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['ColorButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['ColorButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' color'
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\color-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

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
            state=Settings.current_settings['ViewButton']['state'][Settings.theme],
            cursor=Settings.current_settings['ViewButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['ViewButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['ViewButton']['background'][Settings.theme],
            foreground=Settings.current_settings['ViewButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['ViewButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['ViewButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['ViewButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['ViewButton']['activeforeground'][Settings.theme]
        )

        self['text'] = text
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\preview-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

        self.grid(
            column=column, row=row, columnspan=2, rowspan=1,
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
            state=Settings.current_settings['ApplyButton']['state'][Settings.theme],
            cursor=Settings.current_settings['ApplyButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['ApplyButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['ApplyButton']['background'][Settings.theme],
            foreground=Settings.current_settings['ApplyButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['ApplyButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['ApplyButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['ApplyButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['ApplyButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' APPLY'
        self['command'] = self.apply
        self.image = tkinter.PhotoImage(file=r'..\images\apply-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

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
            state=Settings.current_settings['CancelButton']['state'][Settings.theme],
            cursor=Settings.current_settings['CancelButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['CancelButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['CancelButton']['background'][Settings.theme],
            foreground=Settings.current_settings['CancelButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['CancelButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['CancelButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['CancelButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['CancelButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' CANCEL'
        self['command'] = self.cancel
        self.image = tkinter.PhotoImage(file=r'..\images\cancel-white.png')
        self['image'] = self.image
        self['compound'] = 'left'

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def cancel(self):
        self.master.cancel()


class OperationButton(tkinter.Button):

    def __init__(self, master, column, row, action):
        super().__init__(master)

        self.action = action
        self.configure(
            font=Settings.current_settings['OperationButton']['font'],
            state=Settings.current_settings['OperationButton']['state'][Settings.theme],
            cursor=Settings.current_settings['OperationButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['OperationButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['OperationButton']['background'][Settings.theme],
            foreground=Settings.current_settings['OperationButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['OperationButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['OperationButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['OperationButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['OperationButton']['activeforeground'][Settings.theme]
        )

        self['command'] = self.click

        self.image1 = tkinter.PhotoImage(file=r'..\images\save-lightgrey.png')
        self.image2 = tkinter.PhotoImage(file=r'..\images\send-lightgrey.png')
        if self.action == 'save':
            self['image'] = self.image1
            self['text'] = 'SAVE'
        elif self.action == 'send':
            self['image'] = self.image2
            self['text'] = 'SEND'

        self['compound'] = 'bottom'

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
            state=Settings.current_settings['DeleteButton']['state'][Settings.theme],
            cursor=Settings.current_settings['DeleteButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['DeleteButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['DeleteButton']['background'][Settings.theme],
            foreground=Settings.current_settings['DeleteButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['DeleteButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['DeleteButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['DeleteButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['DeleteButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' DEL'
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\delete-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

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
            state=Settings.current_settings['AddButton']['state'][Settings.theme],
            cursor=Settings.current_settings['AddButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['AddButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['AddButton']['background'][Settings.theme],
            foreground=Settings.current_settings['AddButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['AddButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['AddButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['AddButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['AddButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' ADD'
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\add-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

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
            state=Settings.current_settings['OkayButton']['state'][Settings.theme],
            cursor=Settings.current_settings['OkayButton']['cursor'][Settings.theme],
            overrelief=Settings.current_settings['OkayButton']['overrelief'][Settings.theme],
            background=Settings.current_settings['OkayButton']['background'][Settings.theme],
            foreground=Settings.current_settings['OkayButton']['foreground'][Settings.theme],
            borderwidth=Settings.current_settings['OkayButton']['borderwidth'][Settings.theme],
            highlightcolor=Settings.current_settings['OkayButton']['highlightcolor'][Settings.theme],
            activebackground=Settings.current_settings['OkayButton']['activebackground'][Settings.theme],
            activeforeground=Settings.current_settings['OkayButton']['activeforeground'][Settings.theme]
        )

        self['text'] = ' OK'
        self['command'] = self.click
        self.image = tkinter.PhotoImage(file=r'..\images\okay-lightgrey.png')
        self['image'] = self.image
        self['compound'] = 'left'

        self.grid(
            column=column, row=row, columnspan=1, rowspan=1,
            padx=5, pady=5, ipadx=5, ipady=5,
            sticky='WENS'
        )

    def click(self):

        pass
