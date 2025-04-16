from configparser import ConfigParser


def get_config_data(category, key):
    config = ConfigParser()

    config.read('configurations/config.ini')
    return config.get(category, key)
