
logger = logging.getLogger('my_app')

logtofile = logging.FileHandler('logs.log', mode='w+', encoding=None, delay=False)
logtofile.setLevel(logging.INFO)

logtoconsole = logging.StreamHandler(stream=sys.stdout)
logtoconsole.setLevel(logging.DEBUG)

logger.addHandler(logtoconsole)
logger.addHandler(logtofile)

logger.setLevel(logging.DEBUG)
logger.info('The Info Logging')
logger.debug('Debug logging (should not show up in File)')

