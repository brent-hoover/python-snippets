import sys
import logging
DEBUG=True


def main():
    logger = logging.getLogger('my_app')

    logtofile = logging.FileHandler('logs.log', mode='w+', encoding=None, delay=False)
    logtofile.setLevel(logging.INFO)

    logtoconsole = logging.StreamHandler(stream=sys.stdout)
    logtoconsole.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[WEBDEPLOY] %(message)s')
    second_formatter = logging.Formatter('[SECOND_FORMATTER] %(message)s')

    logtoconsole.setFormatter(formatter)
    logtofile.setFormatter(second_formatter)

    logger.addHandler(logtoconsole)
    logger.addHandler(logtofile)

    logger.setLevel(logging.DEBUG)
    logger.info('The Info Logging')
    logger.debug('Debug logging (should not show up in File)')

if __name__ == '__main__':
    main()
