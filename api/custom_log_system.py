import logging


class ColoredFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.colors = {
            logging.DEBUG: "\033[0;37m",  # White
            logging.INFO: "\033[0;32m",  # Green
            logging.WARNING: "\033[0;33m",  # Yellow
            logging.ERROR: "\033[0;31m",  # Red
            logging.CRITICAL: "\033[1;31m",  # Bright Red
        }

    def format(self, record):
        log_color = self.colors.get(record.levelno)
        reset_color = "\033[0m"
        record.msg = f"{log_color}{record.msg}{reset_color}"
        return super().format(record)

