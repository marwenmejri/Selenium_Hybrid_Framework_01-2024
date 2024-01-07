import logging


class LogGen:
    @staticmethod
    def sample_logger():
        logger = logging.getLogger('custom_logger')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s | %(module)s", datefmt='%m/%d/%Y %I:%M:%S %p')
        fh = logging.FileHandler(filename="Logs/logs.log", mode='a')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
