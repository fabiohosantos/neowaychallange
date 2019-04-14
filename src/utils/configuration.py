import os
from configparser import SafeConfigParser


class Config:

    __parser_config = None

    @staticmethod
    def initialise(**kwargs):
        Config.__parser_config = SafeConfigParser()
        p = os.path.dirname(__file__)
        file = os.path.join(p, 'project.config')
        Config.__parser_config.read(file)

    @staticmethod
    def get_value(key):
        return Config.__parser_config.get('properties', key)
