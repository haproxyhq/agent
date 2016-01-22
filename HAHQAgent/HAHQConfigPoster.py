import requests

import config
from HAHQConfigurator import HAHQConfigurator


class HAHQConfigPoster(object):
    """
    this is a light helper class, to send the config data to a server specified in the config.py file, after converting
    it to json from the HAProxy config file, using the HAHQConfigurator class
    """
    def __init__(self, config_string=None, config_file_path=None):
        """
        converts the given string data or file to a config dict

        :param config_string: the HAProxy config file as string
        :param config_file_path: the HAProxy config file path
        """
        if config_file_path:
            config_string = self.stringify_file(config_file_path)

        self.config_data = HAHQConfigurator(config_string=config_string).get_config_data()

    def post_config(self, url, token):
        """
        sends the converted data to the server

        :param url: url of the server
        :param token: token for authentication
        """
        requests.post(url, json=self.config_data)

    def stringify_file(self, file):
        """
        this method returns the content of a file as a string

        :param file: file path
        :return: string
        """
        with open(file, 'r') as config_file:
            return config_file.read()