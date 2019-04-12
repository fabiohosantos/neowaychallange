from configparser import SafeConfigParser

class Config:

    __parser_config = None

    @staticmethod
    def initialise(**kwargs):
        Config.__parser_config = SafeConfigParser()
        Config.__parser_config.read('project.config')

    @staticmethod
    def get_value(key):
        return Config.__parser_config.get('properties', key)
