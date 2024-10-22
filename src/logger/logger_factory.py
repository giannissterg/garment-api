from logger_config import LoggerConfig
from abc import ABC, abstractmethod
import logging


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self, config: LoggerConfig) -> logging.Logger:
        raise NotImplementedError
