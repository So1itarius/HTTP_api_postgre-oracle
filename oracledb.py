import configparser
import os

import cx_Oracle

class OracleProvider:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'))
        self.connect = cx_Oracle.connect(config["Oracle"]["user"],
                                         config["Oracle"]["password"],
                                         config["Oracle"]["address"])
        self.cursor = self.connect.cursor()

