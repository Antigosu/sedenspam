import os
import shutil
import json


class Settings:

    current_settings = None
    settings_directory = os.path.expanduser('~') + '/.sedenspam'
    settings_file = settings_directory + '/settings.json'

    def __init__(self):

        Settings.create()

        # Cache init.
        with open(Settings.settings_file) as file:
            Settings.current_settings = json.load(file)

    @classmethod
    def create(cls):

        if not os.path.isfile(Settings.settings_file):
            os.makedirs(Settings.settings_directory, exist_ok=True)
            shutil.copyfile('default_settings.json', Settings.settings_file)

    @classmethod
    def update(cls):

        with open(Settings.settings_file) as file:
            Settings.current_settings = json.load(file)

        print(Settings.current_settings)
