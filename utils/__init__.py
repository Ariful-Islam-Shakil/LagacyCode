from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import logging
import os
import sys
import json

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LogLevel(Enum):
    """Enum for log levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

@dataclass
class LogMessage:
    """Dataclass for log messages."""
    timestamp: datetime
    level: LogLevel
    message: str

class Logger:
    """Logger class."""
    def __init__(self, name: str, level: LogLevel = LogLevel.INFO):
        """Initialize the logger.

        Args:
            name (str): Logger name.
            level (LogLevel, optional): Logger level. Defaults to LogLevel.INFO.
        """
        self.name = name
        self.level = level
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.value)

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): Message to log.
        """
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): Message to log.
        """
        self._log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): Message to log.
        """
        self._log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): Message to log.
        """
        self._log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): Message to log.
        """
        self._log(LogLevel.CRITICAL, message)

    def _log(self, level: LogLevel, message: str) -> None:
        """Log a message.

        Args:
            level (LogLevel): Log level.
            message (str): Message to log.
        """
        log_message = LogMessage(datetime.now(), level, message)
        self.logger.log(level.value, log_message.message)

def main() -> None:
    """Main function."""
    logger = Logger('main_logger', LogLevel.INFO)
    logger.info('Main program started.')
    logger.debug('Debug message.')
    logger.warning('Warning message.')
    logger.error('Error message.')
    logger.critical('Critical message.')

if __name__ == '__main__':
    main()