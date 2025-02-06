import os
import logging
import colorlog
from datetime import datetime


class CustomFormatter(colorlog.ColoredFormatter):
    """
    Özel log formatı
    """

    def formatTime(self, record, datefmt=None):
        """
        Zaman formatı
        """
        dt = datetime.fromtimestamp(record.created)
        return dt.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

    def format(self, record):
        """
        Log formatı ve renk ayarları
        """
        log_colors = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        }

        # * Full path
        # filename = record.pathname

        # * Only file name
        filename = os.path.basename(record.pathname)

        formatter = colorlog.ColoredFormatter(
            "\n%(log_color)s%(asctime)s - %(levelname)-8s%(reset)s \n  %(filename)s -> %(log_color)s%(message)s%(reset)s\n",
            log_colors=log_colors,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        record.filename = filename
        return formatter.format(record)
