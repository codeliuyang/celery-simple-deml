import logging
from logging.handlers import TimedRotatingFileHandler

outputs_format = [
            "[%(asctime)s | ",
            "%(filename)s, ",
            "%(funcName)s, ",
            "line %(lineno)d | ",
            "%(levelname)s] ",
            "%(message)s",
        ]


def get_db_logger(cls_name="app"):
    logger = logging.getLogger('sqlalchemy.engine')
    filepath = "logs/" + cls_name + ".log"
    handler = logging.handlers.TimedRotatingFileHandler(
        filepath,
        when='midnight',
        backupCount=3
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("".join(outputs_format)))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

