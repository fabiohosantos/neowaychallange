import os
from configparser import SafeConfigParser


class Config:

    __parser_config = None

    @staticmethod
    def initialise(**kwargs):
        Config.__parser_config = SafeConfigParser()
        p = os.path.dirname(__file__)
        Config.__parser_config.read(p + '\project.config')

    @staticmethod
    def get_value(key):
        return Config.__parser_config.get('properties', key)
