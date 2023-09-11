""" utils/logger.py """
import logging


class Logger:
    def __init__(self, debug: bool = False):
        level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d:%H:%M:%S',
                            level=level)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def debug(self, message: str):
        logging.debug(message)

    def error(self, message: str):
        logging.error(message)

    def info(self, message: str):
        logging.info(message)


logger = Logger(True)
