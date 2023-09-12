""" soteriareitti/utils/logging_config.py """
import logging


def configure_logging(debug: bool = False):
    """Configure logging for the globally."""
    level = logging.DEBUG if debug else logging.INFO
    # pylint: disable-next=line-too-long
    logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=level)

    logging.getLogger("urllib3").setLevel(logging.INFO)
    logging.getLogger("PIL.PngImagePlugin").setLevel(logging.INFO)
    logging.getLogger("PIL.Image").setLevel(logging.INFO)
