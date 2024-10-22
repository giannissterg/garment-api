from abc import ABC, abstractmethod
import logging

from .logger_config import LoggerConfig

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self, config: LoggerConfig) -> logging.Logger:
        raise NotImplementedError
