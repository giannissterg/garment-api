import logging

class LoggerConfig:
    def __init__(self, name: str, level=logging.INFO, handlers:list=[], formatter=None):
        self.name = name
        self.level = level
        self.handlers = handlers
        self.formatter = formatter
