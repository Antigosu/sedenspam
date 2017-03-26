import tkinter
import fields.faq
import buttons.email
import buttons.template
import buttons.database
import buttons.settings
import fields.status
import fields.console


class MainWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        faq = fields.faq.FAQField(self)
        faq.enable(column=0, row=1)
        email = buttons.email.PathButton(self)
        email.enable(column=0, row=2)
        template = buttons.template.PathButton(self)
        template.enable(column=0, row=3)
        database = buttons.database.PathButton(self)
        database.enable(column=0, row=4)
        email_status = fields.status.StatusLabel(self)
        email_status.enable(column=1, row=2)
        template_status = fields.status.StatusLabel(self)
        template_status.enable(column=1, row=3)
        database_status = fields.status.StatusLabel(self)
        database_status.enable(column=1, row=4)
        settings = buttons.settings.SettingsButton(self)
        settings.enable(column=1, row=1)
        console = fields.console.ConsoleField(self)
        console.enable(column=3, row=1)
