import logging
import logging.config
import time


def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('leighton_logger')

    logger.info('Program started')
    time.sleep(4)
    logger.info('Done!')


if __name__ == '__main__':
    main()
