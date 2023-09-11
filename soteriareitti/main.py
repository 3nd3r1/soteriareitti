# soteriareitti/main.py
from utils.logging_config import configure_logging
from ui.ui import Ui


def main():
    user_interface = Ui()
    user_interface.run()


if __name__ == "__main__":
    configure_logging()
    main()
