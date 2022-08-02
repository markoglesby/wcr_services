from configparser import ConfigParser
import os
import sys
import subprocess
import time


class Configurator:
    def __init__(self):
        self.congig_file = "wcr_services_config.ini"

    def save_values_from_advanced_settings(self):
        # Config file
        parser = ConfigParser()
        parser.read(self.congig_file)

        parser.set('settings', 'ae', ae_entry.get())
        parser.set('settings', 'version', version.get())
        parser.set('settings', 'aetoken', ae_token.get())

        # Save the config file
        with open('wcr_services_config.ini', 'w') as configfile:
            parser.write(configfile)
