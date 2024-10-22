import logging
from .logger_config import LoggerConfig
from .logger_factory import LoggerFactory


class PyLoggerFactory(LoggerFactory):
    def create_logger(self, config: LoggerConfig) -> logging.Logger:
        """
        Creates and returns a logging.Logger instance with the specified configurations.

        :param config: The configuration of the logger.
        :return: A configured logger instance.
        """
        logger = logging.getLogger(config.name)
        logger.setLevel(config.level)

        # Check if handlers already exist
        if not logger.hasHandlers():
            for handler in config.handlers:
                if config.formatter:
                    handler.setFormatter(config.formatter)
                logger.addHandler(handler)

        return logger

