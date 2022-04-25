import logging

from utils import COLOR


def __formatter() -> logging.Formatter:
    HEADER = '[%(asctime)s - %(levelname)s]'.join(COLOR['GREEN'])
    return logging.Formatter(f"{HEADER} %(message)s")

def __stream_handler() -> logging.StreamHandler:
    handler = logging.StreamHandler()
    handler.setFormatter(__formatter())
    return handler

def __create_logger(name: str = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(__stream_handler())
    logger.propagate = 0
    return logger

logger = __create_logger()

if __name__ == "__main__":
    logger.info("Hello World")