import logging


LOGGING_FORMAT = "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s"
LOGGING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def config_test_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format=LOGGING_FORMAT,
        datefmt=LOGGING_DATE_FORMAT,
    )


config_test_logging()
