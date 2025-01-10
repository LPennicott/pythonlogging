import logging
import logging.config
import time
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_hands = logging.FileHandler('leighton_log.log')
stream_hands = logging.StreamHandler()
logger.addHandler(file_hands)

dateformat = '%Y-%m-%d'
formatting = logging.Formatter(
    ('%(asctime)s == %(levelname)s == %(lineno)d == %(message)s'),
    datefmt=dateformat
)

stream_format = logging.Formatter(
    ('%(asctime)s -- %(name)s -- %(levelname)s -- %(lineno)d -- %(message)s'),
    datefmt=dateformat
)
file_hands.setFormatter(formatting)
stream_hands.setFormatter(stream_format)

logger.addHandler(stream_hands)

logger.debug('this is my first blind logger!')
logger.warning('Two logs at once!')
