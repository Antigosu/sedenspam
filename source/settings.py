import os
import shutil
import json


class Settings:

    current_settings = None

    def __init__(self):

        self.settings_directory = os.path.expanduser('~') + '/.sedenspam'
        self.settings_file = self.settings_directory + '/settings.json'
        self.__create()

        # Cache init.
        with open(self.settings_file) as file:
            Settings.current_settings = json.load(file)

    def __create(self):

        if not os.path.isfile(self.settings_file):
            os.makedirs(self.settings_directory, exist_ok=True)
            shutil.copyfile('default_settings.json', self.settings_file)

    def update(self):

        with open(self.settings_file) as file:
            Settings.current_settings = json.load(file)

        print(Settings.current_settings)
