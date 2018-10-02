from bot import updater
from lib import configure_logging


def start():
    configure_logging()
    updater.start_polling()


if __name__ == '__main__':
    start()
