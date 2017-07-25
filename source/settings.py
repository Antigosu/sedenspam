import os
import shutil
import json


class Settings:

    def __init__(self):

        self.settings_directory = os.path.expanduser('~') + '/.sedenspam'
        self.settings_file = self.settings_directory + '/settings.json'
        self.__create()

        with open(self.settings_file) as file:
            self.settings = json.load(file)

        print(self.settings)

        self.text_color = self.settings['text_color']
        self.is_preview = 1

    def __create(self):

        if not os.path.isfile(self.settings_file):
            os.makedirs(self.settings_directory, exist_ok=True)
            shutil.copyfile('default_settings.json', self.settings_file)

    def update(self):

        with open(self.settings_file) as file:
            self.settings = json.load(file)

        print(self.settings)
