""" soteriareitti/utils/logging_config.py """
import logging


def configure_logging():
    """Configure logging for the globally."""
    logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=logging.DEBUG)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("PIL.PngImagePlugin").setLevel(logging.WARNING)
