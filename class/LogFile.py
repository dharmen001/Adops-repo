# coding=utf-8

"""
logging Class
"""
import logging


class Logger(object):

    def __init__(self):
        self.logger = None

    def logger(self):
        # create logger with 'spam_application'
        """
        logger for console and output
        """
        logger = logging.getLogger('EOCApp')
        logger.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # create file handler which logs even debug messages
        fh = logging.FileHandler('logfile.log'.format())
        fh.setLevel(logging.ERROR)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger


if __name__ == '__main__':
    obj_log = Logger()
    obj_log.logger()