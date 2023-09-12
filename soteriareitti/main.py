# soteriareitti/main.py
import sys

from utils.logging_config import configure_logging
from ui.gui import Gui


def main():
    user_interface = Gui()
    user_interface.run()


if __name__ == "__main__":
    DEBUG = sys.argv[-1] == "debug"
    configure_logging(DEBUG)
    main()
