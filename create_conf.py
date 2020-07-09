import configparser
import os


def createConfig(path):
    """
    Create a config file .ini
    """
    config = configparser.ConfigParser()
    config.add_section("Oracle")
    config.set("Oracle", "user", "")
    config.set("Oracle", "password", "")
    config.set("Oracle", "address", "")
    config.add_section("authentication")
    config.set("authentication", "LOGIN", '')
    config.set("authentication", "PASS", "")

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)
