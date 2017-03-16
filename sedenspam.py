# spam app for my beloved sells managers

import time
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import font
import smtplib
from email.mime.text import MIMEText
from openpyxl import load_workbook


class Application(tk.Frame):
    """
    GUI application for lovely spam letters :3
    """

    def __init__(self, master):
        super().__init__(master)

        self.user = tk.StringVar()

        self.current_user = None
        self.my_address = None
        self.target_address = None
        self.email_server = None
        self.templates = {}

        self.USERS = [
            'Максим',
            'Евгений',
            'Василий',
            'Сергей',
            'Елизавета',
            'Андрей']

        self.EMAILS = [
            'zhenihov@sedmax.ru',
            'eivanov@en-pro.ru',
            'zheltonogov@sedmax.ru',
            'popov@sedmax.ru',
            'laiming@sedmax.ru',
            'avorochalkin@en-pro.ru']

        self.EMAIL_SERVERS = [
            'sedmax.ru',
            'en-pro.ru']

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        best_font = font.Font(family='Verdana', size=10)
        background = 'steelblue3'

        # welcome, my little hooligans
        welcome = tk.Label(
            self,
            text='Добро пожаловать в SED-EN-SPAM!!1\n'
                 'Рассылка спама теперь еще веселее и продуктивнее.',
            font=best_font,
            fg='black',
            bg='bisque3',
            relief='raised',
            borderwidth=1
        )

        welcome.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        spammer = tk.Label(
            self,
            text='Пожалуйста, укажите, как зовут спамера.',
            font=best_font,
            fg='black',
            bg=background,
            relief='ridge',
            borderwidth=2
        )

        spammer.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        # user choice depends on radiobuttons
        self.user.set(None)
        radiobuttons_in_row = 3

        column = 0
        for user in self.USERS[:radiobuttons_in_row]:
            first_row_user = tk.Radiobutton(
                self,
                text=user,
                font=best_font,
                variable=self.user,
                value=user,
                relief='raised',
                borderwidth=3,
                command=self.update_user
            )

            first_row_user.grid(
                row=2,
                column=column,
                columnspan=1,
                sticky='N' + 'S' + 'E' + 'W'
            )
            column += 1

        column = 0
        for user in self.USERS[radiobuttons_in_row:]:
            second_row_user = tk.Radiobutton(
                self,
                text=user,
                font=best_font,
                variable=self.user,
                value=user,
                relief='raised',
                borderwidth=3,
                command=self.update_user
            )

            second_row_user.grid(
                row=3,
                column=column,
                columnspan=1,
                sticky='N' + 'S' + 'E' + 'W'
            )
            column += 1

        # spam base input
        spam = tk.Label(
            self,
            text='Укажите полное (с расширением) название базы:',
            font=best_font,
            fg='black',
            bg=background,
            relief='ridge',
            borderwidth=2
        )

        spam.grid(
            row=5,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        spam_base_name = 'spam_base.xlsx'
        self.emails = tk.Entry(
            self,
            fg='black',
            bg='white',
            font=best_font,
            borderwidth=3
        )

        self.emails.insert(tk.INSERT, spam_base_name)
        self.emails.grid(
            row=6,
            column=0,
            columnspan=3,
            rowspan=1,
            sticky='N' + 'S' + 'E' + 'W'
        )

        # subject and text of a letter
        subject = tk.Label(
            self,
            text='Введите тему письма и текст сообщения, используя'
                 ' специальную форму с {переменными из базы}:',
            font=best_font,
            fg='black',
            bg=background,
            relief='ridge',
            borderwidth=2
        )

        subject.grid(
            row=7,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        default_subject = 'Предложение сотрудничества'
        self.subject = tk.Entry(
            self,
            fg='black',
            bg='white',
            font=best_font,
            borderwidth=3
        )

        self.subject.insert(tk.INSERT, default_subject)
        self.subject.grid(
            row=8,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        with open('default_text.txt') as default:
            default_text = default.read()

        self.text = tkst.ScrolledText(
            self,
            fg='black',
            bg='white',
            font=best_font,
            height=35,
            width=112,
            borderwidth=3
        )

        self.text.insert(tk.INSERT, default_text)
        self.text.grid(
            row=9,
            column=0,
            columnspan=3,
            rowspan=1,
            sticky='N' + 'S' + 'E' + 'W'
        )

        # send spam to all ur victims
        submit_spam = tk.Button(
            self,
            text='Отправить\nрассылку',
            font=best_font,
            fg='black',
            bg='firebrick1',
            relief='raised',
            cursor='exchange',
            borderwidth=3,
            command=self.send_spam
        )

        submit_spam.grid(
            row=10,
            column=0,
            columnspan=3,
            sticky='N' + 'S' + 'E' + 'W'
        )

        # quit button, now u'r clear
        quit_app = tk.Button(
            self,
            text='\nВыход\n',
            font=best_font,
            fg='black',
            bg='bisque3',
            cursor='pirate',
            command=window.destroy
        )

        quit_app.grid(
            row=11,
            column=0,
            columnspan=3,
            rowspan=2,
            sticky='N' + 'S' + 'E' + 'W'
        )

    def update_user(self):
        # user choice
        self.current_user = self.user.get()

    def download_base(self):
        # download spam base here to dict
        self.templates.clear()
        spam_base_name = self.emails.get()
        spam_file = load_workbook(filename=spam_base_name, read_only=True)
        spam_base = spam_file['spam_base']
        cache = {}
        row_number = -1

        for row in spam_base.rows:
            row_number += 1
            template = []
            for cell in row:
                if cell.value:
                    template.append(cell.value)
            cache.setdefault(row_number, template)

        for key in cache.keys():
            if cache[key]:
                self.templates.setdefault(key, cache[key])

    def send_spam(self):
        # send spam there with smtplib
        self.download_base()

        # init user...
        for i in range(len(self.USERS)):
            if self.current_user == self.USERS[i]:
                self.my_address = self.EMAILS[i]

        for i in range(len(self.EMAIL_SERVERS)):
            if self.my_address.endswith(self.EMAIL_SERVERS[i]):
                self.email_server = 'smtp.' + self.EMAIL_SERVERS[i]

        # sending...
        for row_number in range(len(self.templates)):
            if row_number >= 1:
                # TODO: optimise
                message = MIMEText(
                    self.text.get('1.0', 'end').format(
                        position=self.templates[row_number][0],
                        company=self.templates[row_number][1],
                        to_whom=self.templates[row_number][2],
                        sex=self.templates[row_number][3],
                        who=self.templates[row_number][4],
                        place=self.templates[row_number][5]
                    )
                )
                self.target_address = self.templates[row_number][6]

                message['Subject'] = self.subject.get()
                message['From'] = self.my_address
                message['To'] = self.target_address

                letter = smtplib.SMTP(self.email_server)
                # letter.send_message(message)
                letter.quit()
                # TODO: 15-20 seconds
                # time.sleep(20)
                print(self.templates)
                print(message)

# no main func cuz i need to ran app every time
window = tk.Tk()
window.title('sed-en-spam')
window.wm_iconbitmap('sedenspam.ico')
window.configure(background='thistle4')
app = Application(master=window)
app.mainloop()
