import tkinter
from source import labels, buttons, listboxes


class MainFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')  # Different colors for debug.

        # for col_index in range(5):
        #     self.columnconfigure(col_index, weight=1, minsize=150)
        # self.rowconfigure(0, weight=1, minsize=75)

        self.setup_frame = SetupFrame(self)
        self.operation_frame = OperationFrame(self)

        self.pack(side='top', fill='both', expand='yes')


class PreviewFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(background='steelblue')  # Different colors for debug.

        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=300)

        self.rowconfigure(0, weight=1, minsize=300)

        self.template_preview = labels.PreviewLabel(master=self, column=0, row=0)
        self.email_preview = labels.PreviewLabel(master=self, column=1, row=0)

        self.pack(side='top', fill='both', expand='yes')


class SetupFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(background='cyan3')  # Different colors for debug.

        self.columnconfigure(0, weight=1, minsize=225)
        self.columnconfigure(1, weight=1, minsize=75)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.faq_label = labels.FAQLabel(master=self, column=0, row=0)
        self.email_label = labels.UserChoiceLabel(master=self, column=0, row=1)
        self.template_label = labels.UserChoiceLabel(master=self, column=0, row=2)
        self.database_label = labels.UserChoiceLabel(master=self, column=0, row=3)

        self.settings_button = buttons.SettingsButton(master=self, column=1, row=0)
        self.email_button = buttons.UserChoiceButton(master=self, column=1, row=1, data_type='email')
        self.template_button = buttons.UserChoiceButton(master=self, column=1, row=2, data_type='template')
        self.database_button = buttons.UserChoiceButton(master=self, column=1, row=3, data_type='database')

        self.pack(side='left', fill='both', expand='yes')


class OperationFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(background='sienna1')  # Different colors for debug.

        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=1, minsize=150)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.console = labels.ConsoleLabel(master=self, column=0, row=0)

        self.send_button = buttons.OperationButton(master=self, column=0, row=2)
        self.exit_button = buttons.OperationButton(master=self, column=1, row=2)

        self.pack(side='right', fill='both', expand='yes')


class SettingsFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.color = ''
        self.view = ''

        self.configure(background='sienna1')  # Different colors for debug.

        for col_index in range(4):
            self.columnconfigure(col_index, weight=1, minsize=150)

        for row_index in range(4):
            self.rowconfigure(row_index, weight=1, minsize=75)

        self.color_label = labels.SettingsLabel(master=self, column=0, row=0)

        self.color_button = buttons.ColorButton(master=self, column=0, row=1)

        self.with_view_button = buttons.ViewButton(master=self, column=0, row=2, text='WITH\nPREVIEW')
        self.without_view_button = buttons.ViewButton(master=self, column=1, row=2, text='WITHOUT\nPREVIEW')

        self.apply_button = buttons.ApplyButton(master=self, column=0, row=3)
        self.cancel_button = buttons.CancelButton(master=self, column=1, row=3)

        self.pack(side='left', fill='both', expand='yes')

    def apply(self):

        print(self.color)
        print(self.view)

    def cancel(self):

        print('CANCEL')
        self.master.destroy()


class BasicInputFrame(tkinter.Frame):

    def __init__(self, master, data_type):
        super().__init__(master)

        self.data_type = data_type

        self.configure(background='sienna1')  # Different colors for debug.

        for col_index in range(3):
            self.columnconfigure(col_index, weight=1, minsize=150)

        for row_index in range(2):
            self.rowconfigure(row_index, weight=1, minsize=75)

        if self.data_type == 'email':
            self.email_list = listboxes.BasicListbox(master=self, column=0, row=0, data_type=self.data_type)
        elif self.data_type == 'template':
            self.email_list = listboxes.BasicListbox(master=self, column=0, row=0, data_type=self.data_type)
        elif self.data_type == 'database':
            self.email_list = listboxes.BasicListbox(master=self, column=0, row=0, data_type=self.data_type)

        self.delete_button = buttons.DeleteButton(master=self, column=0, row=1)
        self.add_button = buttons.AddButton(master=self, column=1, row=1)
        self.okay_button = buttons.OkayButton(master=self, column=2, row=1)

        self.pack(side='left', fill='both', expand='yes')
